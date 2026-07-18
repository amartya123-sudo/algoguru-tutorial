from langchain_core.prompts import PromptTemplate
from langchain_ollama import AIMessage


def validate(namespace):

    context = namespace.get("context")

    assert context is not None, (
        "Create a variable named 'context'."
    )

    assert isinstance(context, str), (
        "'context' should be a string."
    )

    assert len(context.strip()) > 0, (
        "The retrieved context should not be empty."
    )

    prompt = namespace.get("prompt")

    assert prompt is not None, (
        "Create a variable named 'prompt'."
    )

    assert isinstance(prompt, PromptTemplate), (
        "'prompt' should be a PromptTemplate."
    )

    response = namespace.get("response")

    assert response is not None, (
        "Create a variable named 'response'."
    )

    assert isinstance(response, AIMessage), (
        "The response should be an AIMessage."
    )

    assert len(response.content.strip()) > 0, (
        "The model should generate a response."
    )

    return (
        "Excellent! You built a custom RAG pipeline using LlamaIndex and LangChain."
    )