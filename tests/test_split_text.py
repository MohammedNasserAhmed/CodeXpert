import pytest
from codechat.components.split_text import TextSplitter

@pytest.fixture
def splitter():
    return TextSplitter()

def test_split_text(splitter):
    text = "This is a long document. It needs to be split."
    split_text = splitter.split([text])
    assert isinstance(split_text, list)
    assert len(split_text) > 1 