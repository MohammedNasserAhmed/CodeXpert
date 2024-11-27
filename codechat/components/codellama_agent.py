from typing import Dict, Any
from langgraph.graph import StateGraph, Graph
from langchain_core.messages import HumanMessage, AIMessage
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from typing import Dict, Any, List, Union
from langgraph.graph import StateGraph, Graph
import logging


class AgentState:
    """Represents the state of the code analysis agent."""
    def __init__(self, messages: List[Union[HumanMessage, AIMessage]], next_step: str):
        self.messages = messages
        self.next_step = next_step


class CodeLlamaAgent:
    """
    A class-based, state-of-the-art implementation of a Code Analysis Agent
    using LLM and graph-based workflows.
    """

    def __init__(self, model_name: str = "llama3.1"):
        """
        Initializes the agent with the specified language model.

        Parameters:
        - model_name (str): Name of the model to be used.
        """
        self.llm = Ollama(model=model_name)
        self.workflow = self._create_workflow()
        logging.info(f"CodeLlamaAgent initialized with model: {model_name}")

    def _create_workflow(self) -> Graph:
        """Sets up the workflow graph with tasks and transitions."""
        workflow = StateGraph(AgentState)

        # Adding tasks (nodes)
        workflow.add_node("analyze_code", self._analyze_code)
        workflow.add_node("explain_result", self._explain_result)
        workflow.add_node("suggest_improvements", self._suggest_improvements)

        # Adding transitions (edges)
        workflow.add_edge("analyze_code", "explain_result")
        workflow.add_edge("explain_result", "suggest_improvements")
        workflow.set_entry_point("analyze_code")

        return workflow.compile()

    def _analyze_code(self, state: AgentState) -> AgentState:
        """Analyzes the given code using the language model."""
        messages = state.messages
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a code analysis expert. Analyze the following code and provide insights."),
            ("human", "{input}")
        ])
        response = self._run_chain(prompt, messages[-1].content)
        messages.append(AIMessage(content=response))
        state.next_step = "explain_result"
        return state

    def _explain_result(self, state: AgentState) -> AgentState:
        """Explains the result of the code analysis in simpler terms."""
        messages = state.messages
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert at explaining technical concepts. Explain the following analysis in simpler terms."),
            ("human", "{input}")
        ])
        response = self._run_chain(prompt, messages[-1].content)
        messages.append(AIMessage(content=response))
        state.next_step = "suggest_improvements"
        return state

    def _suggest_improvements(self, state: AgentState) -> AgentState:
        """Suggests improvements for the analyzed code."""
        messages = state.messages
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a software optimization expert. Suggest improvements for the following code and analysis."),
            ("human", "{input}")
        ])
        response = self._run_chain(prompt, "\n".join([m.content for m in messages]))
        messages.append(AIMessage(content=response))
        state.next_step = "end"
        return state

    def _run_chain(self, prompt: ChatPromptTemplate, input_text: str) -> str:
        """Runs a chain of prompts through the LLM."""
        try:
            chain = prompt | self.llm
            logging.info("Running LLM chain...")
            response = chain.invoke({"input": input_text})
            logging.info("Chain execution successful.")
            return response
        except Exception as e:
            logging.error(f"Error in running chain: {e}")
            raise

    def run(self, code: str) -> Dict[str, Any]:
        """
        Runs the agent workflow on the given code.

        Parameters:
        - code (str): The source code to analyze.

        Returns:
        - Dict[str, Any]: Contains the analysis, explanation, and improvement suggestions.
        """
        initial_state = AgentState(
            messages=[HumanMessage(content=code)],
            next_step="analyze_code"
        )
        logging.info("Starting workflow...")
        result = self.workflow.invoke(initial_state.__dict__)
        logging.info("Workflow completed successfully.")

        return {
            "analysis": result['messages'][1].content,
            "explanation": result['messages'][2].content,
            "improvements": result['messages'][3].content
        }
