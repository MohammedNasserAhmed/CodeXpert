import os
from typing import List, Optional, Union, Callable
from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from codeexp.config.constants import DOCS_DIR

from langchain_community.document_loaders import (
    DirectoryLoader, 
    TextLoader, 
    PyPDFLoader, 
    Docx2txtLoader,
    CSVLoader,
    JSONLoader,
    UnstructuredMarkdownLoader
)
from langchain_core.documents import Document
from pydantic import BaseModel, Field, validator

class DocumentLoaderConfig(BaseModel):
    """Configuration model for document loading."""
    root_dir: Path
    file_types: List[str] = Field(
        default_factory=lambda: ['.txt', '.pdf', '.docx', '.csv', '.json', '.md'],
        description="Supported file types for loading"
    )
    recursive: bool = True
    ignore_hidden: bool = True
    max_workers: int = os.cpu_count() or 1
    
    @validator('root_dir')
    def validate_root_dir(cls, v):
        """Validate that the root directory exists."""
        if not v.exists() or not v.is_dir():
            raise ValueError(f"Invalid directory path: {v}")
        return v

class DocumentLoader:
    """
    An advanced, extensible document loader with multiple features:
    - Multi-threaded document loading
    - Flexible file type support
    - Logging
    - Error handling
    - Configurable loading parameters
    """
    
    # Mapping of file extensions to appropriate loaders
    LOADER_MAPPING = {
        '.txt': TextLoader,
        '.pdf': PyPDFLoader,
        '.docx': Docx2txtLoader,
        '.csv': CSVLoader,
        '.json': JSONLoader,
        '.md': UnstructuredMarkdownLoader
    }
    
    def __init__(
        self, 
        config: Optional[DocumentLoaderConfig] = None,
        custom_loaders: Optional[dict] = None,
        file_names: Optional[list]= None
    ):
        """
        Initialize the document loader with optional configuration and custom loaders.
        
        :param config: Configuration for document loading
        :param custom_loaders: Additional custom loaders for specific file types
        """
        self.config = config or DocumentLoaderConfig(root_dir=Path('.'))
        self.logger = self._setup_logger()
        self.file_names = file_names
        
        # Update loader mapping with custom loaders
        if custom_loaders:
            self.LOADER_MAPPING.update(custom_loaders)
    
    def _setup_logger(self) -> logging.Logger:
        """
        Set up a structured logger for document loading operations.
        
        :return: Configured logger instance
        """
        # Remove existing handlers to prevent duplicate logging
        logger = logging.getLogger(self.__class__.__name__)
        
        # Clear any existing handlers
        if logger.handlers:
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)
        
        logger.setLevel(logging.INFO)
        
        # Create console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        ch.setFormatter(formatter)
        
        # Prevent adding duplicate handlers
        if not logger.handlers:
            logger.addHandler(ch)
        
        # Prevent propagation to root logger
        logger.propagate = False
        
        return logger
    
    def _get_loader_for_file(self, file_path: Path) -> Callable:
        """
        Determine the appropriate loader for a given file path.
        
        :param file_path: Path to the file
        :return: Loader class for the file
        """
        file_ext = file_path.suffix.lower()
        loader_cls = self.LOADER_MAPPING.get(
            file_ext, 
            TextLoader  # Default to TextLoader if no specific loader found
        )
        
        return lambda: loader_cls(str(file_path), autodetect_encoding=True)
    
    def _load_single_document(self, file_path: Path) -> List[Document]:
        """
        Load a single document with error handling.
        
        :param file_path: Path to the document
        :return: List of loaded documents
        """
        try:
            loader = self._get_loader_for_file(file_path)()
            return loader.load()
        except Exception as e:
            self.logger.error(f"Error loading document {file_path}: {e}")
            return []
    
    def load_documents(
        self, 
        file_filter: Optional[Callable[[Path], bool]] = None
    ) -> List[Document]:
        """
        Load documents from the specified directory with advanced features.
        
        :param file_filter: Optional function to filter files
        :return: List of loaded documents
        """
        import time
        
        start_time = time.time()
        
        # Only log if not already logged in this session
        if not hasattr(self, '_loading_logged'):
            self.logger.info(f"Starting document loading from {self.config.root_dir}")
            self._loading_logged = True
        
        # Find all files matching criteria
        all_files = [
            f for f in self.config.root_dir.rglob('*') 
            if (f.is_file() and 
                (not self.config.ignore_hidden or not f.name.startswith('.')) and
                f.suffix.lower() in self.config.file_types and
                (file_filter is None or file_filter(f))
            )
        ]
        self.file_names=[f.stem for f in all_files]
        # Multi-threaded document loading
        documents = []
        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            future_to_file = {
                executor.submit(self._load_single_document, file): file 
                for file in all_files
            }
            
            for future in as_completed(future_to_file):
                file = future_to_file[future]
                try:
                    doc_batch = future.result()
                    documents.extend(doc_batch)
                except Exception as e:
                    self.logger.error(f"Unexpected error processing {file}: {e}")
        
        elapsed_time = time.time() - start_time
        
        # Only log if not already logged in this session
        if not hasattr(self, '_completion_logged'):
            self.logger.info(
                f"Loaded {len(documents)} documents from {len(all_files)} files "
                f"in {elapsed_time:.2f} seconds"
            )
            self._completion_logged = True
        
        return documents
    
    def save_documents(
        self, 
        documents: List[Document], 
        format: str = 'txt'
    ) -> None:
        """
        Save loaded documents to an output directory.
        
        :param documents: List of documents to save
        :param output_dir: Directory to save documents
        :param format: Output file format
        """
        output_path = Path(DOCS_DIR)
        output_path.mkdir(parents=True, exist_ok=True)
        
        for idx, doc in enumerate(documents):
            file_path = output_path / f"{self.file_names[idx]}.{format}"
            try: 
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(doc.page_content)
                self.logger.info(f"Saved document to {file_path}")
            except Exception as e:
                self.logger.error(f"Error saving document {idx}: {e}")

