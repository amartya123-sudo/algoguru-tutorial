def validate(namespace):

    chat_history = namespace.get("chat_history")

    assert chat_history is not None, (
        "Create a variable named 'chat_history'."
    )

    assert isinstance(chat_history, list), (
        "'chat_history' should be a list."
    )

    assert len(chat_history) >= 2, (
        "Store both the user question and assistant response in 'chat_history'."
    )

    context = namespace.get("context")

    assert context is not None, (
        "Create a variable named 'context'."
    )

    assert isinstance(context, str), (
        "'context' should be a string."
    )

    response = namespace.get("response")

    assert response is not None, (
        "Create a variable named 'response'."
    )

    assert hasattr(response, "content"), (
        "The response should contain generated content."
    )

    assert len(response.content.strip()) > 0, (
        "The generated response should not be empty."
    )

    return (
        "Excellent! You built a conversational RAG assistant that combines retrieval with chat history."
    )