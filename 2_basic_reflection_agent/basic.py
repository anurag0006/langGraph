from typing import List, Sequence
from dotenv import load_dotenv
load_dotenv() 
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generation_chain, reflection_chain
# message graph maintains a list of messages and decides the folow of those messages bw the nodes
# Every ndoe in messsage graph receives the full list of preiovus messages as input
# each node can append new messages to the list and return it


graph = MessageGraph()

REFLECT = "reflect"
GENERATE = "generate"

def generate_node(state):
    return generation_chain.invoke({
        "messages": state
    })

def reflect_node(state):
    response = reflection_chain.invoke({
        "messages": state
    })
    return [HumanMessage(content=response.content)]



graph.add_node(GENERATE,generate_node)
graph.add_node(REFLECT,reflect_node)
graph.set_entry_point(GENERATE)

def should_continue(state):
    if(len(state) > 6):
        return END
    return REFLECT



graph.add_conditional_edges(
    GENERATE,
    should_continue,
    {
        REFLECT: REFLECT,
        END: END
    }
)

graph.add_edge(REFLECT, GENERATE)   

app = graph.compile()

print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()



response = app.invoke(HumanMessage(content="Write a tweet about LangGraph."))

print(response)