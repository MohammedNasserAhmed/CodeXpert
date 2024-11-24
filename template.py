# template.py
import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'code_rag'

list_of_files = [
    # GitHub workflow
    ".github/workflows/.gitkeep",
    
    # Source code structure
    f"src/{project_name}/__init__.py",
    
    # Components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/document_processor.py",
    f"src/{project_name}/components/vector_store.py",
    f"src/{project_name}/components/llm_agent.py",
    
    # Utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/helpers.py",
    
    # Configuration
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/constants.py",
    
    # Pipeline
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/rag_pipeline.py",
    
    # Entity
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    
    # Constants
    f"src/{project_name}/constants/__init__.py",
    
    # Tests
    "tests/__init__.py",
    "tests/test_document_processor.py",
    "tests/test_vector_store.py",
    "tests/test_llm_agent.py",
    
    # Data directories
    "data/codebase/.gitkeep",
    "data/vector_store/.gitkeep",
    
    # Configuration files
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    
    # Project files
    "requirements.txt",
    "setup.py",
    "README.md",
    
    # App files
    "app.py",
    
    # Notebooks
    "notebooks/trials.ipynb",
    
    # Templates
    "templates/index.html"
]

def generate_config_yaml():
    """Generate default config.yaml content"""
    config_content = """
# Project Configuration
project:
  name: code_rag
  version: 1.0.0

# Model Configuration
model:
  repo_id: codellama/CodeLlama-7b-hf
  temperature: 0.1
  max_length: 512

# Vector Store Configuration
vector_store:
  path: ./data/vector_store
  collection_name: code_chunks
  chunk_size: 1000
  chunk_overlap: 200

# Paths Configuration
paths:
  codebase: ./data/codebase
  vector_store: ./data/vector_store
"""
    return config_content

def generate_setup_py():
    """Generate setup.py content"""
    setup_content = """
from setuptools import setup, find_packages

setup(
    name="code_rag",
    version="1.0.0",
    author="M. N. Gaber",
    author_email="abunasserip@gmail.com.com",
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
"""
    return setup_content

def generate_readme():
    """Generate README.md content"""
    readme_content = """# Code RAG System using CodeLlama and Qdrant

This project implements a Retrieval-Augmented Generation (RAG) system for code analysis using CodeLlama and Qdrant.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

3. Configure the system:
   - Update `config/config.yaml` with your settings
   - Place your codebase in the `data/codebase` directory

4. Run the application:
   ```bash
   streamlit run app.py
   ```
"""
    return readme_content

# Create project structure
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            # Add content to specific files
            if filename == "config.yaml":
                f.write(generate_config_yaml())
            elif filename == "setup.py":
                f.write(generate_setup_py())
            elif filename == "README.md":
                f.write(generate_readme())
        logging.info(f"Creating {'empty ' if filename not in ['config.yaml', 'setup.py', 'README.md'] else ''}file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

logging.info("Project template created successfully!")
logging.info("\nNext steps:")
logging.info("1. Create a virtual environment: python -m venv venv")
logging.info("2. Activate the virtual environment")
logging.info("3. Install the package: pip install -e .")
logging.info("4. Update config/config.yaml with your settings")
logging.info("5. Run the application: streamlit run app.py")