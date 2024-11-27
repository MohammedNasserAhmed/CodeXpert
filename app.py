from codechat.pipeline.rag_pipeline import CodeAnalysisPipeline
import logging

pipeline = CodeAnalysisPipeline()

PHASE_NAME= "Load and preprocess documents"
logging.info(f">>>>>> phase {PHASE_NAME} started <<<<<<") 
pipeline.load_and_preprocess_documents()

PHASE_NAME=  "Create embeddings and vector store"
logging.info(f">>>>>> phase {PHASE_NAME} started <<<<<<") 
pipeline.create_embeddings_and_vector_store()

PHASE_NAME = "Initialize QA chain and explanation chain"
logging.info(f">>>>>> phase {PHASE_NAME} started <<<<<<") 
pipeline.initialize_qa_chain()
pipeline.initialize_agent_and_explanation_chain()

PHASE_NAME = "Process user query"
logging.info(f">>>>>> phase {PHASE_NAME} started <<<<<<") 
user_query = "Explain the purpose of the provided code"
if user_query:
    pipeline.process_query(user_query)