import pytest
from codexpert.components.llm_agent import QAChain
from unittest.mock import MagicMock

@pytest.fixture
def qachain():
    return QAChain(repo_id="dummy-repo")

def test_initialize_llm(qachain):
    llm = qachain.initialize_llm()
    assert llm is not None

def test_get_qa_chain(qachain):
    mock_retriever = MagicMock()
    qa_chain = qachain.get_qa_chain(retriever=mock_retriever)
    assert qa_chain is not None
