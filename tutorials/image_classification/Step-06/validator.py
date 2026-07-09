import torch.nn as nn


def validate(namespace):

    model = namespace.get("model")

    assert model is not None, \
        "Create an instance named model."

    assert isinstance(model, nn.Module), \
        "SimpleCNN must inherit from nn.Module."

    assert hasattr(model, "conv1"), \
        "Define conv1."

    assert hasattr(model, "pool"), \
        "Define pool."

    assert hasattr(model, "fc1"), \
        "Define fc1."

    return "Excellent! CNN created successfully."