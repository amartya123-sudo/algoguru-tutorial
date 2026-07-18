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

llm = ChatOllama(
    model="llama3.2",
)

chat_history = []

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
Conversation:
{history}

Context:
{context}

Question:
{question}

Answer:
"""
)

formatted_prompt = prompt.format(
    history="\n".join(chat_history),
    context=context,
    question=question,
)

response = llm.invoke(
    formatted_prompt,
)

chat_history.append(
    f"User: {question}"
)

chat_history.append(
    f"Assistant: {response.content}"
)

print(response.content)