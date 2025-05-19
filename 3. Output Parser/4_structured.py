from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os

load_dotenv()
if "GROQ_API_KEY" not in os.environ:
    print("GROQ_API_KEY not found") 

model = ChatGroq(
    model="llama-3.1-8b-instant", 
)  

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)


# problem: We cant add validations (Data types etc)  