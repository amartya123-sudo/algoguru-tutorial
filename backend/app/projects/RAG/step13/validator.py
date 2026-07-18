from langchain_core.prompts import PromptTemplate


def validate(namespace):

    prompt = namespace.get("prompt")

    assert prompt is not None, (
        "Create a variable named 'prompt'."
    )

    assert isinstance(prompt, PromptTemplate), (
        "'prompt' should be a PromptTemplate."
    )

    formatted_prompt = namespace.get(
        "formatted_prompt"
    )

    assert formatted_prompt is not None, (
        "Create a variable named 'formatted_prompt'."
    )

    assert isinstance(formatted_prompt, str), (
        "'formatted_prompt' should be a string."
    )

    assert "Python is a programming language." in formatted_prompt, (
        "The context should appear in the formatted prompt."
    )

    assert "What is Python?" in formatted_prompt, (
        "The question should appear in the formatted prompt."
    )

    return (
        "Excellent! You created and formatted your first LangChain prompt."
    )