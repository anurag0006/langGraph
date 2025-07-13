from typing import TypedDict
from langgraph.graph import END,StateGraph

class SimpleState(TypedDict):
    count: int


def increment(state: SimpleState) -> SimpleState:
    """Increment the count in the state."""
    state['count'] += 1
    return state

def should_continue(state: SimpleState) -> bool:
    """Check if the count is less than 5."""
    if(state["count"] < 5):
        return "continue"
    else:
        return "stop"
    
graph = StateGraph(SimpleState)

graph.add_node("increment", increment)
graph.add_node("should_continue", should_continue)  
graph.add_conditional_edges("increment", should_continue,{
    "continue": "increment",
    "stop": END
})
graph.set_entry_point("increment")

app = graph.compile()


result = app.invoke(SimpleState(count=0))

print(result)