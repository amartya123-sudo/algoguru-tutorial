def validate(namespace):

    model = namespace.get("model")
    optimizer = namespace.get("optimizer")

    assert model is not None, \
        "Model was not created."

    assert optimizer is not None, \
        "Optimizer was not created."

    loss = namespace.get("loss")

    assert loss is not None, \
        "Compute the loss."

    outputs = namespace.get("outputs")

    assert outputs is not None, \
        "Run a forward pass."

    return "Excellent! The training loop executed successfully."