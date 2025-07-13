from llm_client import llm
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from langchain.agents import initialize_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import Tool
import datetime

# Create the time function
def get_current_time(input_str: str = "") -> str:
    """Get the current system time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create tool using Tool class
get_system_time = Tool(
    name="get_system_time",
    description="Get the current system time",
    func=get_current_time
)

search_tool = TavilySearchResults(search_depth="basic")
agent = initialize_agent(
    tools=[search_tool, get_system_time], 
    llm=llm, 
    agent="zero-shot-react-description", 
    verbose=True
)

agent.invoke("When was ScapeX's last funding round? What is the current time?")