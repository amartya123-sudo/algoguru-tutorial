def validate(namespace):

    dataset = namespace.get("dataset")


    assert dataset is not None, (
        "Create a variable named 'dataset' using one of: "
        "datasets.MNIST, datasets.FashionMNIST, "
        "datasets.CIFAR10, or datasets.KMNIST."
    )

    from torchvision.datasets import (
        MNIST,
        FashionMNIST,
        CIFAR10,
        KMNIST,
    )

    allowed = (
        MNIST,
        FashionMNIST,
        CIFAR10,
        KMNIST,
    )

    assert isinstance(dataset, allowed), \
        (
            "Choose one of: "
            "MNIST, FashionMNIST, CIFAR10, KMNIST"
        )

    return (
        f"Excellent! "
        f"You loaded {dataset.__class__.__name__}."
    )