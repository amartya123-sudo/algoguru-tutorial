def validate(namespace):

    nodes = namespace.get("nodes")

    assert nodes is not None, (
        "Create a variable named 'nodes'."
    )

    assert isinstance(nodes, list), (
        "'nodes' should be a list."
    )

    assert len(nodes) > 0, (
        "Split the documents into one or more nodes."
    )

    first_node = nodes[0]

    assert hasattr(first_node, "text"), (
        "Each node should contain text."
    )

    assert isinstance(first_node.text, str), (
        "The node text should be a string."
    )

    assert len(first_node.text.strip()) > 0, (
        "The node text should not be empty."
    )

    return (
        f"Excellent! You created {len(nodes)} nodes from your documents."
    )