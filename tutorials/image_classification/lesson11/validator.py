import torch.nn as nn


def validate(namespace):

    loaded_model = namespace.get("loaded_model")

    assert loaded_model is not None, \
        "Create a variable named loaded_model."

    assert isinstance(
        loaded_model,
        nn.Module,
    ), "loaded_model must be a PyTorch model."

    assert loaded_model.training is False, \
        "Call loaded_model.eval()."

    return "Excellent! Model saved and loaded successfully."