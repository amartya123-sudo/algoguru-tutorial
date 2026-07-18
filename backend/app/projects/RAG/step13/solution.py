from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    """
You are a helpful assistant.

Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""
)

formatted_prompt = prompt.format(
    context="Python is a programming language.",
    question="What is Python?",
)

print(formatted_prompt)