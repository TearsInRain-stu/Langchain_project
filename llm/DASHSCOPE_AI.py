from Langchain.llm.AI_API import DASHSCOPE_API
from langchain_openai import ChatOpenAI

whale_ai = ChatOpenAI(
    api_key=DASHSCOPE_API,
    model="qwen-plus",     
    base_url="",                                                  # Enter your AI's base_url
)

from Langchain.medicine.medicine_schema import Medicine

structed_whale_ai=whale_ai.with_structured_output(Medicine)

"""
What does with with_structured_output?
Purpose:It make AI return a object to your pydantic class(like ChatResponse) you make

Typical usage in FastAPI:
 1.Define a pydantic class
 2.Wrap your model with with_structured_output()
 3.Call.invoke() -> You Can get a instance of ChatResponse
 4.Return it in your route -> FastAPI  validates&converts to JSON

 Attention:
 your model must support Function Calling
"""
