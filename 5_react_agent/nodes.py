from dotenv import load_dotenv
from langgraph.prebuilt.tool_executor import ToolExecutor

from agent_reason_runnable import react_agent_runnable, tools
from react_state import AgentState

load_dotenv()

def reason_node(state: AgentState):
    agent_outcome = react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}

tool_executor = ToolExecutor(tools)  # Fixed typo: tool_exector -> tool_executor

def act_node(state: AgentState):
    agent_action = state["agent_outcome"]
    output = tool_executor.invoke(agent_action)
    
    # Append to existing intermediate_steps instead of overwriting
    current_steps = state.get("intermediate_steps", [])
    return {"intermediate_steps": current_steps + [(agent_action, output)]}