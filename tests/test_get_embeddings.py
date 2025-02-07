import pytest
from coderag.components.get_embeddings import Embedding
from unittest.mock import patch


@pytest.fixture
def embedder():
    return Embedding(model_name="dummy-model")


def test_get_embeddings():
    # Mock the embedding response
    embeddings = embedder.get_embeddings()
    assert embeddings == [0.1, 0.2, 0.3]
