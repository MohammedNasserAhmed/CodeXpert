from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
import logging


class QAChain:
    """
    A state-of-the-art manager for setting up Retrieval-based QA systems
    using HuggingFaceHub LLMs and retrievers.
    """

    def __init__(self, repo_id: str, temperature: float = 0.5, max_length: int = 500):
        """
        Initializes the QAChainManager with an LLM from HuggingFaceHub.

        Parameters:
        - repo_id (str): The HuggingFace repository ID for the model.
        - temperature (float): The sampling temperature for the model.
        - max_length (int): Maximum token length for the model output.
        """
        self.repo_id = repo_id
        self.temperature = temperature
        self.max_length = max_length
        self.llm = None
        self.qa_chain = None
        logging.info(
            f"QAChain initialized with model: {repo_id}, "
            f"temperature: {temperature}, max_length: {max_length}"
        )

    def initialize_llm(self):
        """Initializes the HuggingFaceHub LLM."""
        try:
            logging.info("Initializing LLM from HuggingFaceHub...")
            self.llm = HuggingFaceHub(
                repo_id=self.repo_id,
                model_kwargs={
                    "temperature": self.temperature,
                    "max_length": self.max_length,
                },
            )
            logging.info("LLM successfully initialized.")
            return self.llm
        except Exception as e:
            logging.error(f"Error initializing LLM: {e}")
            raise

    def get_qa_chain(self, retriever):
        """
        Sets up the QA chain with the initialized LLM and retriever.

        Parameters:
        - retriever: A retriever instance to provide context to the QA chain.

        Returns:
        - RetrievalQA: The initialized QA chain.
        """
        if not self.llm:
            logging.error("LLM is not initialized. Please call initialize_llm() first.")
            raise ValueError("LLM is not initialized.")
        try:
            logging.info("Setting up QA chain...")
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm, chain_type="stuff", retriever=retriever
            )
            logging.info("Returning the QA chain instance.")
        except Exception as e:
            logging.error(f"Error setting up QA chain: {e}")
            raise

        return self.qa_chain

    
