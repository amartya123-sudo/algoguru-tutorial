import torch.nn as nn
import torch.optim as optim


def validate(namespace):

    model = namespace.get("model")
    criterion = namespace.get("criterion")
    optimizer = namespace.get("optimizer")

    assert model is not None, \
        "Create a variable named model."

    assert isinstance(model, nn.Module), \
        "model must be a PyTorch neural network."

    assert criterion is not None, \
        "Create a variable named criterion."

    assert isinstance(criterion, nn.CrossEntropyLoss), \
        "Use nn.CrossEntropyLoss()."

    assert optimizer is not None, \
        "Create a variable named optimizer."

    assert isinstance(optimizer, optim.Adam), \
        "Use optim.Adam()."

    assert optimizer.defaults["lr"] == 0.001, \
        "Use a learning rate of 0.001."

    return "Excellent! Loss function and optimizer configured successfully."