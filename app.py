import streamlit as st
import logging
from codexpert.pipeline.rag_pipeline import CodeAnalysisPipeline

# Configure logging
logging.basicConfig(level=logging.INFO)


def main():
    st.title("CodeXpert Analysis Pipeline")

    # Initialize pipeline
    pipeline = CodeAnalysisPipeline()

    # Phase 1: Load and preprocess documents
    st.header("Phase 1: Load and preprocess documents")
    if st.button("Start Phase 1"):
        try:
            phase_name = "Load and preprocess documents"
            st.write(f">>>>>> phase {phase_name} started <<<<<<")
            pipeline.load_and_preprocess_documents()
            st.success("Phase 1 completed successfully")
        except Exception as e:
            st.error(f"Error in phase {phase_name}: {e}")

    # Phase 2: Create embeddings and vector store
    st.header("Phase 2: Create embeddings and vector store")
    if st.button("Start Phase 2"):
        try:
            phase_name = "Create embeddings and vector store"
            st.write(f">>>>>> phase {phase_name} started <<<<<<")
            pipeline.create_embeddings_and_vector_store()
            st.success("Phase 2 completed successfully")
        except Exception as e:
            st.error(f"Error in phase {phase_name}: {e}")

    # Phase 3: Initialize QA chain and explanation chain
    st.header("Phase 3: Initialize QA chain and explanation chain")
    if st.button("Start Phase 3"):
        try:
            phase_name = "Initialize QA chain and explanation chain"
            st.write(f">>>>>> phase {phase_name} started <<<<<<")
            pipeline.initialize_qa_chain()
            pipeline.initialize_agent_and_explanation_chain()
            st.success("Phase 3 completed successfully")
        except Exception as e:
            st.error(f"Error in phase {phase_name}: {e}")

    # Phase 4: Process user query
    st.header("Phase 4: Process user query")
    user_query = st.text_input(
        "Enter your query", "Explain the purpose of the provided code"
    )
    if st.button("Start Phase 4"):
        try:
            phase_name = "Process user query"
            st.write(f">>>>>> phase {phase_name} started <<<<<<")
            if user_query:
                response = pipeline.process_query(user_query)
                st.write("Response:", response)
                st.success("Phase 4 completed successfully")
        except Exception as e:
            st.error(f"Error in phase {phase_name}: {e}")


if __name__ == "__main__":
    main()
