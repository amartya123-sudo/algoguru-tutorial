def validate(namespace):

    response = namespace.get("response")

    assert response is not None, (
        "Create a variable named 'response'."
    )

    response_text = str(response)

    assert len(response_text.strip()) > 0, (
        "The response should not be empty."
    )

    return (
        "Excellent! You generated an answer using the Query Engine."
    )