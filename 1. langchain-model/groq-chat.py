from langchain_groq import ChatGroq 
from dotenv import load_dotenv
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

result = llm.invoke("What is the difference between a LLM and a ChatModel?")

print(result.content)