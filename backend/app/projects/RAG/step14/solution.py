from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

documents = SimpleDirectoryReader(
    input_dir="data",
).load_data()

index = VectorStoreIndex.from_documents(
    documents,
)

retriever = index.as_retriever(
    similarity_top_k=2,
)

question = "What is Python?"

results = retriever.retrieve(
    question,
)

context = "\n\n".join(
    node.text
    for node in results
)

prompt = PromptTemplate.from_template(
    """
Answer the question using only
the provided context.

Context:
{context}

Question:
{question}

Answer:
"""
)

formatted_prompt = prompt.format(
    context=context,
    question=question,
)

llm = ChatOllama(
    model="llama3.2",
)

response = llm.invoke(
    formatted_prompt,
)

print(response.content)