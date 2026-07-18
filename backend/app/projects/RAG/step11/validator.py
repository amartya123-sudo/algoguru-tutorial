def validate(namespace):

    results = namespace.get("results")

    assert results is not None, (
        "Create a variable named 'results'."
    )

    assert isinstance(results, list), (
        "'results' should be a list."
    )

    assert len(results) > 0, (
        "Retrieve at least one node."
    )

    first_result = results[0]

    assert hasattr(first_result, "text"), (
        "Each retrieved result should contain text."
    )

    assert isinstance(first_result.text, str), (
        "The retrieved text should be a string."
    )

    return (
        f"Excellent! You retrieved {len(results)} relevant node(s)."
    )