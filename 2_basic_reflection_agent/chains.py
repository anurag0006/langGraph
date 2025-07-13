import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from common.llm_client import llm





generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellenet twitter posts"
            "Gnerate the best writter post possible for the user's request"
            "If the user provides critique, respond with a revised version of your previous attempts"
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet"
            "Always provide detailed recommendations, including requests for length, virality, style, etc",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm

