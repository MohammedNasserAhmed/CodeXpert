# Code RAG System using CodeLlama and Qdrant

This project implements a Retrieval-Augmented Generation (RAG) system for code analysis using CodeLlama and Qdrant.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
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
