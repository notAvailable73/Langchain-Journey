from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

load_dotenv()
if "GROQ_API_KEY" not in os.environ:
    print("GROQ_API_KEY not found") 

model = ChatGroq(
    model="llama-3.1-8b-instant", 
)  
 

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# problem: we cant  specify the key names.