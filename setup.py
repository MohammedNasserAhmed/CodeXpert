
from setuptools import setup, find_packages

setup(
    name="code_chat",
    version="1.0.0",
    author="M. N. Gaber",
    author_email="abunasserip@gmail.com",
    description="Code RAG Chat",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit>=1.24.0",
        "langchain>=0.0.200",
        "qdrant-client>=1.1.1",
        "huggingface-hub>=0.14.1",
        "transformers>=4.30.2",
        "python-dotenv>=1.0.0"
    ],
    python_requires=">=3.8",
)
