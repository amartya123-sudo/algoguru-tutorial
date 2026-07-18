def validate(namespace):

    documents = namespace.get("documents")

    assert documents is not None, (
        "Create a variable named 'documents'."
    )

    first_document = namespace.get("first_document")

    assert first_document is not None, (
        "Create a variable named 'first_document'."
    )

    assert first_document == documents[0], (
        "'first_document' should reference the first document."
    )

    assert hasattr(first_document, "text"), (
        "The document should have a 'text' attribute."
    )

    assert isinstance(first_document.text, str), (
        "'text' should be a string."
    )

    assert len(first_document.text.strip()) > 0, (
        "The document text should not be empty."
    )

    assert hasattr(first_document, "metadata"), (
        "The document should have a 'metadata' attribute."
    )

    assert isinstance(first_document.metadata, dict), (
        "'metadata' should be a dictionary."
    )

    return (
        "Excellent! You explored the contents of a LlamaIndex Document."
    )