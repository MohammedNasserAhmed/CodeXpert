<p align="center">
  <img src="https://github.com/user-attachments/assets/0b4052bd-2b06-4456-96ea-3d5da751c493" alt="Project Logo" width="350" height="150">
</p>

<div align="center">

# CodeXpert with CodeLlama & FAISS 🧠

</div>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.9%2B-white" alt="Python 3.9+">
  </a>
  <img src="https://img.shields.io/badge/CodeLlama-3.1-yellow?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA..." alt="CodeLlama">
  <img src="https://img.shields.io/badge/FAISS-1.7.3-green?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA..." alt="FAISS">
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-orange?logo=huggingface" alt="HuggingFace">
  <img src="https://img.shields.io/badge/License-Apache-blue" alt="License">
</p>

---

**Welcome** to the **CodeExp**, an advanced, state-of-the-art framework designed to analyze, explain, and optimize Python codebases. This repository leverages **CodeLlama**, **LangChain**, and **FAISS** to deliver a seamless, interactive experience for code comprehension and improvement.

---
<p align="center">
  <img src="https://github.com/user-attachments/assets/69a5f6a4-f62b-4f8e-94de-e986fea1423b" alt="Project Architecture" width="800" height="400">
</p>

---

## 🚀 **Purpose**

The **Code Analysis Pipeline** provides an automated solution for:
- **Code Understanding**: Analyze Python code for functionality and structure.
- **Knowledge Extraction**: Generate clear and actionable insights using LLMs.
- **Code Optimization**: Suggest performance improvements and best practices.
- **Technical Education**: Simplify complex code concepts for learners and professionals.

---

## 🎯 **Techniques & Workflow**

1. **Document Loading & Splitting**:
   - Recursively scans the specified directory for Python files.
   - Splits large files into manageable chunks for efficient processing.
2. **Semantic Embedding Generation**:
   - Extracts embeddings using a HuggingFace embedding model.
3. **Vector Store Creation**:
   - Builds a FAISS vector store for semantic search and retrieval.
4. **Question Answering (QA)**:
   - Processes user queries through a **QA Chain** with a retriever.
5. **Code Analysis & Explanation**:
   - Analyzes results using **CodeLlama** and simplifies explanations with templates.
6. **Improvement Suggestions**:
   - Leverages LLMs to suggest actionable optimizations.

---

## ✨ **Features**

- 📂 **Recursive Document Loading**: Processes entire directories with customizable file extensions.
- ✂️ **Text Splitting**: Splits large files into smaller chunks for precise embeddings.
- 🧠 **Advanced Embedding Models**: Uses HuggingFace's embeddings for high-quality vector representations.
- 🔍 **Efficient Retrieval**: Semantic search powered by FAISS.
- 🦙 **LLM-Powered Analysis**: Code analysis and explanations via CodeLlama.
- 📈 **Optimization Suggestions**: Provides practical tips for code improvements.
- 🔗 **Seamless Integration**: Designed to integrate with other AI tools and pipelines.

---

## 🛠 **Technologies**

| Technology           | Purpose                                |
|----------------------|----------------------------------------|
| **LangChain**        | Modular framework for building LLM-based workflows. |
| **FAISS**            | Vector similarity search for efficient code retrieval. |
| **CodeLlama**        | Advanced code understanding via LLMs.  |
| **HuggingFace Hub**  | Hosting and serving LLMs and embeddings. |
| **Python**           | Primary programming language.          |

---

## 📋 **Getting Started**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/MohammedNasserAhmed/CodeXpert.git
cd code-analysis-pipeline
```

### 2️⃣ **Install Dependencies**
Install required libraries with:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Set Environment Variables**
Create a `.env` file or export these variables directly:
```bash
MODEL=<YOUR_LLAMA_MODEL_VERSION>
HUGGINGFACEHUB_API_TOKEN=<Your_HuggingFace_Token>
REPO_ID=<Your_HuggingFace_Repo_ID>
CODEBASE_DIR=<Path_to_Your_Codebase>
EMBEDDING_MODEL=<HuggingFace_Embedding_Model>
```

### 4️⃣ **Run the Pipeline**
```bash
python app.py
```

### 5️⃣ **Interact with the Agent**
Provide a query like:
```plaintext
How to replace FAISS with CHORMA .
```

---

## 🌟 **Pipeline Architecture**

```plaintext
+--------------------+       +--------------------+       +----------------------+
| Document Loader    |-----> | Text Splitter      |-----> | Embedding Generator  |
+--------------------+       +--------------------+       +----------------------+
                                                         |
                                                         v
                                    +----------------------------------+
                                    | FAISS Vector Store               |
                                    +----------------------------------+
                                                         |
                                                         v
                                    +----------------------------------+
                                    | Retrieval-Based QA Chain         |
                                    +----------------------------------+
                                                         |
                                                         v
                            +--------------------------------------------+
                            | CodeLlama Agent for Analysis & Explanations |
                            +--------------------------------------------+
                                                         |
                                                         v
                                   +----------------------------------+
                                   | Suggestions for Code Improvement |
                                   +----------------------------------+
```



---

### 📂 **Project Structure**


```
CodeExp/
│
├── codeexp/
│   ├── components/
│   │   ├── load_document.py           # Handles >> document loading from the codebase
│   │   ├── split_text.py              # Splits >> documents into manageable chunks
│   │   ├── get_embeddings.py          # Generates >> embeddings using HuggingFace models
│   │   ├── codellama_agent.py         # Code analysis agent >> powered by Llama models
│   │   ├── vector_store.py            # Manages >> FAISS vector store initialization
│   │   ├── llm_agent.py               # Handles LLM setup and question-answering
│   │
│   ├── config/
│   │   ├── constants.py               # Contains >> configurations like API tokens and file paths
│
├── tests/                             # Contains >> unit tests for all components
│   ├── test_load_document.py          # Tests >> for the document loader
│   ├── test_split_text.py             # Tests >> for the text splitter
│   ├── test_get_embeddings.py         # Tests >> for the embedding generator
│   ├── test_codellama_agent.py        # Tests >> for the CodeLlama agent
│   ├── test_vector_store.py           # Tests >> for the FAISS vector store
│   └── test_llm_agent.py              # Tests >> for the LLM setup and QA chain
│
├── .gitignore                         # Specifies >> files and folders to ignore in version control
├── requirements.txt                   # Dependencies >> required for the project
├── README.md                          # Project documentation (you are here!)
```

---

### 🔍 **Run Tests**
To verify the functionality of the components, use `pytest`:

Run all tests:
```bash
pytest CodeXpert/tests/
```

Run tests with detailed output:
```bash
pytest -v
```

Run tests for a specific component:
```bash
pytest CodeXpert/tests/test_<component_name>.py
```

Generate a coverage report (requires `pytest-cov`):
```bash
pip install pytest-cov
pytest --cov=CodeXpert/codechat
```

---

## 🎓 **Use Cases**

- **Developers**: Enhance understanding of complex codebases.
- **Educators**: Provide clear code explanations for learners.
- **Researchers**: Analyze algorithmic code for optimization.
- **Organizations**: Maintain clean, optimized, and well-documented repositories.

---

## 🛡 **Best Practices**

- **File Types**: Ensure the target codebase contains supported extensions (e.g., `.py`).
- **Environment Setup**: Use a virtual environment to isolate dependencies.
- **Model Performance**: Adjust embedding and LLM parameters for optimal results.

---

## 🤝 **Contributing**

We welcome contributions! If you'd like to improve the pipeline, please:
1. Fork this repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with a detailed description.

---

## 🔧 **Project Maintenance**

### Key Maintainer
- **[M. N. Gaber](https://github.com/MohammedNasserAhmed)**

---

## 📜 **License**

This project is licensed under the Apache License. See the `LICENSE` file for details.

---

## 🌐 **Contact**

Feel free to reach out for questions or feedback:
- 📧 **Email**: abunasserip@gmail.com
- 🐦 **LinkedIn**: [@M.N.Gaber](https://linkedin.com/in/m-n-g)

---

## 🏆 **Acknowledgments**

Special thanks to:
- **HuggingFace** for hosting world-class AI models.
- **LangChain** for simplifying LLM workflows.
- **FAISS** for fast and efficient retrieval.

---

**🚀 Ready to revolutionize code analysis? Dive in today and supercharge your development process! 🦾**
