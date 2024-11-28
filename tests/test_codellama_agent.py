import pytest
from codexpert.components.codellama_agent import CodeLlamaAgent

@pytest.fixture
def agent():
    return CodeLlamaAgent(model_name="llama3.1")

def test_agent_run(agent):
    code_analysis = "def add(a, b): return a + b"
    result = agent.run(code_analysis)
    assert "analysis" in result
    assert "explanation" in result
    assert "improvements" in result
