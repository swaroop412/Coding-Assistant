from dotenv import  load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from prompts import *
from states import *
llm = ChatGroq(model="openai/gpt-oss-120b")

user_prompt = "create a simple calculator web application"


prompt = planner_prompt(user_prompt)

resp = llm.with_structured_output(Plan).invoke(prompt)

print(resp)