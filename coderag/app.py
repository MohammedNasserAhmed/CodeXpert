import os
import logging
from coderag.config.constants import HUGGINGFACE_TOKEN, CODEBASE_DIR, EMBEDDING_MODEL
from coderag.components.load_document import DocumentLoader, DocumentLoaderConfig
from coderag.components.split_text import TextSplitter
from coderag.components.llm_agent import QAChain
from coderag.components.get_embeddings import Embedding
from coderag.components.codellama_agent import CodeLlamaAgent
from coderag.components.vector_store import VectorStore

# Set up environment variables and logging
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACE_TOKEN
logging.basicConfig(level=logging.INFO)


class CodeAnalysisPipeline:
    def __init__(self):
        self.config = DocumentLoaderConfig(
            root_dir=CODEBASE_DIR,
            file_types=[".py"],  # Add your file extensions here
        )
        self.document_loader = DocumentLoader(self.config)
        self.text_splitter = TextSplitter()
        self.embedding = Embedding(model_name=EMBEDDING_MODEL)
        self.vector_store = VectorStore()
        self.qa_chain = QAChain()
        self.code_llama_agent = CodeLlamaAgent()

    def run_pipeline(self):
        logging.info("Starting the code analysis pipeline...")
        documents = self.document_loader.load_documents()
        logging.info(f"Loaded {len(documents)} documents.")

        split_texts = self.text_splitter.split(documents)
        logging.info(f"Split documents into {len(split_texts)} chunks.")

        embeddings = self.embedding.get_embeddings(split_texts)
        logging.info("Generated embeddings for the text chunks.")

        self.vector_store.store_embeddings(embeddings)
        logging.info("Stored embeddings in the vector store.")

        # Example query processing
        query = "Explain the purpose of the provided code"
        response = self.qa_chain.process_query(query)
        logging.info(f"Query response: {response}")

        return response


if __name__ == "__main__":
    pipeline = CodeAnalysisPipeline()
    pipeline.run_pipeline()
