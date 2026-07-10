def validate(namespace):

    dataset = namespace.get("dataset")


    assert dataset is not None, (
        "Create a variable named 'dataset' using one of: "
        "datasets.MNIST, datasets.FashionMNIST, "
        " or datasets.KMNIST."
    )

    from torchvision.datasets import (
        MNIST,
        FashionMNIST,
        KMNIST,
    )

    allowed = (
        MNIST,
        FashionMNIST,
        KMNIST,
    )

    assert isinstance(dataset, allowed), \
        (
            "Choose one of: "
            "MNIST, FashionMNIST, KMNIST"
        )

    return (
        f"Excellent! "
        f"You loaded {dataset.__class__.__name__}."
    )