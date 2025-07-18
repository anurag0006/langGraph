import operator
from typing import TypedDict, Annotated, Union

from langchain_core.agents import AgentAction, AgentFinish

class AgentState(TypedDict):
    """State for the agent."""
    input: str
    agent_outcome : Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction,str]], operator.add]