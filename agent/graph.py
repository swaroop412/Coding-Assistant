from dotenv import  load_dotenv
from langsmith.schemas import Prompt
from pydantic import BaseModel, Field
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b")

user_prompt = "create a simple calculator web application"


prompt = f"""
You are the PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan

User request: {user_prompt}
"""



class Plan(BaseModel):
    name:str = Field(description="The name of the app tp be built")
    description: str = Field(description="The description of the app tp be built")
resp = llm.with_structured_output(Plan).invoke(prompt)

print(resp)