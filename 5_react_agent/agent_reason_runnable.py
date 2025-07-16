import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from common.llm_client import llm
from langchain.agents import create_react_agent,tool
from langchain_community.tools import TavilySearchResults
import datetime
from langchain import hub
search_tool = TavilySearchResults(search_depth="basic")


@tool
def get_system_time(input_str: str = "") -> str:
    """Get the current system time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


tools = [search_tool, get_system_time]

react_prompt = hub.pull("hwchase17/react")

react_agent_runnable = create_react_agent(tools=tools, llm=llm, verbose=True)