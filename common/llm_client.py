from langchain_openai import AzureChatOpenAI
import os

from pydantic import BaseModel, Field

class Country(BaseModel):
    """Information about a country"""
    name: str = Field(description="The name of the country" )
    capital: str = Field(description="The capital city of the country")
    area: float = Field(description="The total area of the country in square kilometers")       
    population: int = Field(description="The total population of the country")  



deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # If using env var for deployment name
api_version = os.environ["AZURE_OPENAI_API_VERSION"]  # Check your API version on Azure

llm = AzureChatOpenAI(
    azure_deployment=deployment_name or "o3-mini",  # Replace with your actual deployment name
    api_version=api_version,  # Check your API version on Azure
    # temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# llm = llm.with_structured_output(Country)
# res = llm.invoke("Tell me about India")
# print(res)