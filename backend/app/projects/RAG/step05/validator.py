def validate(namespace):

    nodes = namespace.get("nodes")

    assert nodes is not None, (
        "Create a variable named 'nodes'."
    )

    first_node = namespace.get("first_node")

    assert first_node is not None, (
        "Create a variable named 'first_node'."
    )

    assert first_node == nodes[0], (
        "'first_node' should reference the first node."
    )

    assert hasattr(first_node, "text"), (
        "The node should contain text."
    )

    assert isinstance(first_node.text, str), (
        "'text' should be a string."
    )

    assert len(first_node.text.strip()) > 0, (
        "The node text should not be empty."
    )

    assert hasattr(first_node, "metadata"), (
        "The node should contain metadata."
    )

    assert isinstance(first_node.metadata, dict), (
        "'metadata' should be a dictionary."
    )

    return (
        "Excellent! You explored the contents of a node."
    )