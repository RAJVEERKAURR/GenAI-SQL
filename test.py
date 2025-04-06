from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

#Define the template and prompt

template="""User has given a question below. Answer it.
| {question}"""
prompt=ChatPromptTemplate.from_template(template)


# Set up the model

model=ChatOllama(temperature=0, model="llama3.2")

#Create the Chain

chain=prompt|model
response=chain.invoke({"question":"Tell me something about Finance?"})

print(response.content)