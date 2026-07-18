def validate(namespace):

    documents = namespace.get("documents")

    assert documents is not None, (
        "Create a variable named 'documents'."
    )

    assert isinstance(documents, list), (
        "'documents' should be a list."
    )

    assert len(documents) >= 2, (
        "Load at least two documents from the data directory."
    )

    return (
        f"Excellent! You loaded {len(documents)} documents."
    )