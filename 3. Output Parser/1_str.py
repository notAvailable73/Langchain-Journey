from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()
if "GROQ_API_KEY" not in os.environ:
    print("GROQ_API_KEY not found") 

model = ChatGroq(
    model="llama-3.1-8b-instant", 
)  

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)

