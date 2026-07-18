from llama_index.core import VectorStoreIndex


def validate(namespace):

    index = namespace.get("index")

    assert index is not None, (
        "Create a variable named 'index'."
    )

    assert isinstance(index, VectorStoreIndex), (
        "'index' should be a VectorStoreIndex."
    )

    return (
        "Excellent! You created your first VectorStoreIndex."
    )