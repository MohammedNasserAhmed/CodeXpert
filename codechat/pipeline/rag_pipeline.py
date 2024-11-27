import os
import logging
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from codechat.config.constants import REPO_ID, HUGGINGFACE_TOKEN, CODEBASE_DIR, EMBEDDING_MODEL, MODEL
from codechat.components.load_document import DocumentLoader, DocumentLoaderConfig
from codechat.components.split_text import TextSplitter
from codechat.components.llm_agent import QAChain
from codechat.components.get_embeddings import Embedding
from codechat.components.codellama_agent import CodeLlamaAgent
from codechat.components.vector_store import VectorStore

# Set up environment variables and logging
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACE_TOKEN
logging.basicConfig(level=logging.INFO)

class CodeAnalysisPipeline:
    def __init__(self):
        self.config = DocumentLoaderConfig(
            root_dir=CODEBASE_DIR,
            file_types=['.py'],  # Add your file extensions
            recursive=True
        )
        self.documents = None
        self.texts = None
        self.vector_store = None
        self.retriever = None
        self.llm = None
        self.qa_chain = None
        self.explanation_chain = None
        self.agent = None

    def load_and_preprocess_documents(self):
        """Loads and preprocesses documents."""
        logging.info("Loading documents...")
        loader = DocumentLoader(self.config)
        self.documents = loader.load_documents()
        loader.save_documents(self.documents)

        logging.info("Splitting documents...")
        splitter = TextSplitter()
        self.texts = splitter.split(self.documents)

    def create_embeddings_and_vector_store(self):
        """Creates embeddings and initializes the vector store."""
        logging.info("Generating embeddings...")
        embedder = Embedding(model_name=EMBEDDING_MODEL)
        embeddings = embedder.get_embeddings()

        logging.info("Initializing vector store...")
        vector_store_handler = VectorStore()
        self.vector_store = vector_store_handler.initialize_faiss_store(self.texts, embeddings)
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 1})

    def initialize_qa_chain(self):
        """Initializes the QA chain."""
        logging.info("Initializing QA chain...")
        qachain_manager = QAChain(repo_id=REPO_ID)
        self.llm = qachain_manager.initialize_llm()
        self.qa_chain = qachain_manager.get_qa_chain(retriever=self.retriever)

    def initialize_agent_and_explanation_chain(self):
        """Sets up the explanation chain and code analysis agent."""
        logging.info("Setting up explanation chain...")
        explanation_template = """
        Analyze and explain the following result:
        {result}

        Please provide:
        1. A summary of the main points
        2. Any technical concepts mentioned and their explanations
        3. Potential implications or applications of this information
        """
        explanation_prompt = PromptTemplate(template=explanation_template, input_variables=["result"])
        self.explanation_chain = LLMChain(llm=self.llm, prompt=explanation_prompt)

        logging.info("Initializing CodeLlama agent...")
        self.agent = CodeLlamaAgent(model_name=MODEL)

    def process_query(self, query: str):
        """Processes a user query through the QA chain, agent, and explanation chain."""
        logging.info("Processing query through QA chain...")
        result = self.qa_chain.run(query)

        logging.info("Running agent analysis...")
        agent_result = self.agent.run(result)

        # Output results
        print("Answer:")
        print(result)

        print("AI Agent Analysis:")
        print(agent_result['analysis'])

        print("AI Agent Explanation:")
        print(agent_result['explanation'])

        print("AI Agent Suggested Improvements:")
        print(agent_result['improvements'])

        # Retrieve relevant documents
        logging.info("Retrieving relevant documents...")
        docs = self.retriever.get_relevant_documents(query)
        for i, doc in enumerate(docs):
            logging.info(f"Analyzing document {i + 1}...")
            doc_analysis = self.agent.run(doc.page_content)

            print(f"Document {i + 1} Analysis:")
            print(doc_analysis['analysis'])
            print(doc_analysis['explanation'])
            print(doc_analysis['improvements'])
            print("---")

