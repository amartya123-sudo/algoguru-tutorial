def validate(namespace):

    vector_store = namespace.get("vector_store")

    assert vector_store is not None, (
        "Create a variable named 'vector_store'."
    )

    assert isinstance(vector_store, list), (
        "'vector_store' should be a list."
    )

    assert len(vector_store) > 0, (
        "The vector store should contain one or more records."
    )

    first_record = vector_store[0]

    assert isinstance(first_record, dict), (
        "Each record should be a dictionary."
    )

    assert "text" in first_record, (
        "Each record should contain 'text'."
    )

    assert "embedding" in first_record, (
        "Each record should contain 'embedding'."
    )

    assert "metadata" in first_record, (
        "Each record should contain 'metadata'."
    )

    assert isinstance(first_record["embedding"], list), (
        "'embedding' should be a list."
    )

    return (
        f"Excellent! You created a vector store with "
        f"{len(vector_store)} records."
    )