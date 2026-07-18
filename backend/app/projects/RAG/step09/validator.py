def validate(namespace):

    best_match = namespace.get("best_match")

    assert best_match is not None, (
        "Create a variable named 'best_match'."
    )

    assert isinstance(best_match, dict), (
        "'best_match' should be a dictionary."
    )

    assert "text" in best_match, (
        "The matched record should contain 'text'."
    )

    assert "embedding" in best_match, (
        "The matched record should contain 'embedding'."
    )

    assert "metadata" in best_match, (
        "The matched record should contain 'metadata'."
    )

    assert isinstance(best_match["text"], str), (
        "'text' should be a string."
    )

    assert len(best_match["text"].strip()) > 0, (
        "The matched text should not be empty."
    )

    return (
        "Excellent! You retrieved the most relevant document using semantic search."
    )