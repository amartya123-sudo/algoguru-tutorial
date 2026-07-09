import torch


def validate(namespace):

    image = namespace.get("image")

    predicted = namespace.get("predicted")

    model = namespace.get("model")

    assert model.training is False, \
        "Call model.eval()."

    assert isinstance(image, torch.Tensor), \
        "Transform the image into a tensor."

    assert image.dim() == 4, \
        "Add a batch dimension using unsqueeze(0)."

    assert predicted is not None, \
        "Predict the class."

    return "Excellent! Single image prediction completed."