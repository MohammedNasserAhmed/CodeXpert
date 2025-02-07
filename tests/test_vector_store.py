import pytest
from coderag.components.vector_store import VectorStore
from unittest.mock import MagicMock, patch


@pytest.fixture
def vector_store():
    return VectorStore()


def test_initialize_faiss_store(vector_store):
    mock_texts = ["text1", "text2", "text3"]
    mock_embeddings = [0.1, 0.2, 0.3]

    # Mock the FAISS store initialization
    with patch(
        "codexpert.components.vector_store.VectorStore.initialize_faiss_store",
        return_value=MagicMock(),
    ) as mock_faiss:
        vector_store.initialize_faiss_store(mock_texts, mock_embeddings)
        mock_faiss.assert_called_once()
