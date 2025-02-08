from langchain_community.vectorstores import FAISS
from typing import List, Any
from config.constants import DOCS_DIR


class VectorStore:
    """
    A state-of-the-art utility for initializing vector stores using FAISS.
    """

    def __init__(self, logger: Any = None):
        """
        Initializes the VectorStore with an optional logger.

        Args:
            logger (Any): Optional logger for tracking the process.
        """
        self.logger = logger or self._default_logger()

    def initialize_faiss_store(self, texts: List[str], embeddings=List[str]) -> FAISS:
        """
        Sets up the FAISS vector store with the provided texts and embeddings.

        Args:
            texts (List[str]): A list of textual documents to be embedded and stored.

        Returns:
            FAISS: The initialized FAISS vector store.

        Raises:
            ValueError: If the input texts are invalid.
            Exception: If FAISS initialization fails.
        """
        # Validate input
        if not texts or not isinstance(texts, list) or len(texts) == 0:
            raise ValueError("The 'texts' provided for FAISS are empty or invalid.")

        if self.logger:
            self.logger.info(
                f"Initializing FAISS with {len(texts)} documents using embeddings: {self.embeddings}."
            )

        try:
            # Initialize FAISS vector store
            vector_store = FAISS.from_documents(documents=texts, embedding=embeddings)

            vector_store.save_local(DOCS_DIR)

            if self.logger:
                self.logger.info(
                    "FAISS vector store initialized and saved successfully!"
                )

            return vector_store
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error initializing FAISS vector store: {e}")
            raise

    @staticmethod
    def _default_logger():
        """Fallback logger for basic logging."""
        import logging

        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)
