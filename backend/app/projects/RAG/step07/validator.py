def validate(namespace):

    score = namespace.get("score")

    assert score is not None, (
        "Create a variable named 'score'."
    )

    assert isinstance(score, float), (
        "'score' should be a floating-point number."
    )

    assert -1.0 <= score <= 1.0, (
        "Cosine similarity should be between -1 and 1."
    )

    return (
        f"Excellent! The cosine similarity score is {score:.3f}."
    )