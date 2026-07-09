from torchvision import transforms


def validate(namespace):

    transform = namespace.get("transform")

    assert transform is not None, \
        "Create a variable named transform."

    assert isinstance(transform, transforms.Compose), \
        "Use transforms.Compose()."

    pipeline = transform.transforms

    assert any(
        isinstance(t, transforms.Resize)
        for t in pipeline
    ), "Add transforms.Resize()."

    assert any(
        isinstance(t, transforms.ToTensor)
        for t in pipeline
    ), "Add transforms.ToTensor()."

    assert any(
        isinstance(t, transforms.Normalize)
        for t in pipeline
    ), "Add transforms.Normalize()."

    return "Excellent! Image preprocessing pipeline created successfully."