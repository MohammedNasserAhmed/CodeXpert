from langchian_community.embeddings import HuggingFaceEmbeddings
import logging

class Embedding:
    """
    A state-of-the-art class to manage HuggingFace embeddings initialization with modularity and flexibility.
    """

    def __init__(self, model_name=None, **kwargs):
        """
        Initializes the Embedding.

        Parameters:
        - model_name (str): Name of the HuggingFace model for embeddings.
        - kwargs: Additional arguments for the HuggingFaceEmbeddings.
        """
        self.model_name = model_name
        self.kwargs = kwargs
        self._embeddings = None
        logging.info(f"EmbeddingManager initialized with model: {self.model_name}")

    def get_embeddings(self):
        """
        Lazy loads and returns HuggingFace embeddings.

        Returns:
        - HuggingFaceEmbeddings: The embeddings object.
        """
        if self._embeddings is None:
            try:
                logging.info(f"Loading embeddings for model: {self.model_name}")
                self._embeddings = HuggingFaceEmbeddings(model_name=self.model_name, **self.kwargs)
                logging.info("Embeddings successfully loaded.")
            except Exception as e:
                logging.error(f"Error initializing embeddings: {e}")
                raise
        else:
            logging.info("Returning cached embeddings.")
        return self._embeddings

    def reload_embeddings(self, model_name=None):
        """
        Reloads embeddings with a new model name or reinitializes with the same model.

        Parameters:
        - model_name (str): Optional new model name. If not provided, reloads the existing model.
        """
        self.model_name = model_name or self.model_name
        self._embeddings = None
        logging.info(f"Embeddings reloaded with model: {self.model_name}")
