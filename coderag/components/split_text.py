from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict, Any

class TextSplitter:
    """A state-of-the-art text splitting utility for handling large documents."""

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50, logger: Any = None):
        """
        Initialize the TextSplitter with configurable parameters.
        
        Args:
            chunk_size (int): The maximum size of each text chunk.
            chunk_overlap (int): The overlap size between consecutive chunks.
            logger (Any): Optional logger for tracking the process.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.logger = logger or self._default_logger

    def split(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Splits a list of documents into smaller chunks.
        
        Args:
            documents (List[Dict[str, Any]]): A list of documents to be split, 
                                              where each document is a dictionary 
                                              with keys like 'content' or 'text'.
        
        Returns:
            List[Dict[str, Any]]: A list of split document chunks.
        """
        if not documents or not isinstance(documents, list):
            raise ValueError("Invalid input: 'documents' should be a non-empty list.")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, 
            chunk_overlap=self.chunk_overlap
        )

        try:
            if self.logger:
                self.logger.info(f"Splitting {len(documents)} documents with chunk_size={self.chunk_size} and chunk_overlap={self.chunk_overlap}.")

            chunks = text_splitter.split_documents(documents)

            if self.logger:
                self.logger.info(f"Successfully split documents into {len(chunks)} chunks.")

            return chunks
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error during text splitting: {e}")
            raise

    @staticmethod
    def _default_logger():
        """Fallback logger if none is provided."""
        import logging
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)


