import sys
import os
import logging

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from coderag.pipeline.rag_pipeline import CodeAnalysisPipeline

# Configure logging
logging.basicConfig(level=logging.INFO)


def main():
    pipeline = CodeAnalysisPipeline()

    try:
        phase_name = "Load and preprocess documents"
        logging.info(f">>>>>> phase {phase_name} started <<<<<<")
        pipeline.load_and_preprocess_documents()
    except Exception as e:
        logging.error(f"Error in phase {phase_name}: {e}")
        return

    try:
        phase_name = "Create embeddings and vector store"
        logging.info(f">>>>>> phase {phase_name} started <<<<<<")
        pipeline.create_embeddings_and_vector_store()
    except Exception as e:
        logging.error(f"Error in phase {phase_name}: {e}")
        return

    try:
        phase_name = "Initialize QA chain and explanation chain"
        logging.info(f">>>>>> phase {phase_name} started <<<<<<")
        pipeline.initialize_qa_chain()
        pipeline.initialize_agent_and_explanation_chain()
    except Exception as e:
        logging.error(f"Error in phase {phase_name}: {e}")
        return

    try:
        phase_name = "Process user query"
        logging.info(f">>>>>> phase {phase_name} started <<<<<<")
        user_query = "Explain the purpose of the provided code"  # Consider getting this from a config file or environment variable
        if user_query:
            pipeline.process_query(user_query)
    except Exception as e:
        logging.error(f"Error in phase {phase_name}: {e}")
        return


if __name__ == "__main__":
    main()
