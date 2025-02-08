import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_documents(root_dir: str):
    """Loads documents from a specified directory."""
    loader = DirectoryLoader(
        root_dir,
        glob="**/*.*",
        loader_cls=TextLoader,
        loader_kwargs={"autodetect_encoding": True},
    )
    return loader.load()


def split_text(documents):
    """Splits documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_documents(documents)


def initialize_vector_store(texts, embeddings, faiss_path="faiss"):
    """Sets up the FAISS vector store with documents and embeddings."""
    # Ensure the FAISS path exists
    if not os.path.exists(faiss_path):
        os.makedirs(faiss_path)

    # Debugging: Check if texts and embeddings are valid
    if not texts or not isinstance(texts, list) or len(texts) == 0:
        raise ValueError("The 'texts' provided for FAISS are empty or invalid.")

    print(f"Embedding model: {embeddings}")
    print(f"Number of text chunks: {len(texts)}")

    # Ensure texts are not empty
    if len(texts) > 0:
        try:
            return FAISS.from_documents(texts, embeddings)
        except Exception as e:
            print(f"Error initializing FAISS vector store: {e}")
            raise
    else:
        raise ValueError("No text chunks available to process.")


def get_embeddings():
    """Initializes HuggingFace embeddings."""
    return HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
