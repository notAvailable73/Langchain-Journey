from langchain_groq import ChatGroq 
from dotenv import load_dotenv
from typing import TypedDict,List
import getpass
import os

load_dotenv()
if "GROQ_API_KEY" not in os.environ:
    print("GROQ_API_KEY not found") 

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    # model="gemma2-9b-it"
    # other params...
)

 


class Movie(TypedDict):
    Release_Date: str
    Director: str  

structured_model = llm.with_structured_output(Movie)


# result = llm.invoke()
result = structured_model.invoke("""Provide me info about titanic movie""")

print(result)
