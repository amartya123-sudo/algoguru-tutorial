def validate(namespace):

    documents = namespace.get("documents")

    assert documents is not None, (
        "Create a variable named 'documents' using "
        "SimpleDirectoryReader."
    )

    assert isinstance(documents, list), (
        "'documents' should be a list."
    )

    assert len(documents) > 0, (
        "Load at least one document."
    )

    document = documents[0]

    assert hasattr(document, "text"), (
        "Each loaded document should contain a 'text' attribute."
    )

    assert isinstance(document.text, str), (
        "The document text should be a string."
    )

    assert len(document.text.strip()) > 0, (
        "The loaded document should not be empty."
    )

    return (
        "Excellent! You successfully loaded your first "
        "document using LlamaIndex."
    )