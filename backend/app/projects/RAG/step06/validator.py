def validate(namespace):

    embedding = namespace.get("embedding")

    assert embedding is not None, (
        "Create a variable named 'embedding'."
    )

    assert isinstance(embedding, list), (
        "'embedding' should be a list."
    )

    assert len(embedding) > 0, (
        "The embedding should not be empty."
    )

    assert all(
        isinstance(value, float)
        for value in embedding
    ), (
        "The embedding should contain floating-point numbers."
    )

    return (
        f"Excellent! You generated a {len(embedding)}-dimensional embedding."
    )