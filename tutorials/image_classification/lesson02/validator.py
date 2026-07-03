def validate(namespace):

    dataset = namespace.get("dataset")

    assert dataset is not None, \
        "Create a variable named dataset."

    from torchvision.datasets import ImageFolder

    assert isinstance(dataset, ImageFolder), \
        "Use ImageFolder."

    return "Excellent! Dataset loaded successfully."