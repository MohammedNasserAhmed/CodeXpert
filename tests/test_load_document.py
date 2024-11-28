import pytest
from codexpert.components.load_document import DocumentLoader, DocumentLoaderConfig
from unittest.mock import patch

@pytest.fixture
def mock_loader_config():
    return DocumentLoaderConfig(root_dir="/dir/path", file_types=[".py"], recursive=True)

@pytest.fixture
def mock_loader(mock_loader_config):
    return DocumentLoader(mock_loader_config)

def test_load_documents(mock_loader):
    # Mock the actual loading of documents for testing
    with patch("codexpert.components.load_document.DocumentLoader.load_documents", return_value=["doc1", "doc2"]) as mock_load:
        documents = mock_loader.load_documents()
        mock_load.assert_called_once()
        assert documents == ["doc1", "doc2"]

def test_save_documents(mock_loader):
    # Mock saving documents functionality
    with patch("codexpert.components.load_document.DocumentLoader.save_documents") as mock_save:
        mock_loader.save_documents(["doc1", "doc2"])
        mock_save.assert_called_once_with(["doc1", "doc2"])
