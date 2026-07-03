def validate(namespace):

    dataset = namespace.get("dataset")

    assert dataset is not None, \
        "Dataset not found."

    assert hasattr(dataset, "classes"), \
        "ImageFolder should contain classes."

    assert len(dataset.classes) > 0, \
        "Dataset contains no classes."

    assert len(dataset) > 0, \
        "Dataset contains no images."

    return "Excellent! You explored the dataset."