from torch.utils.data import DataLoader


def validate(namespace):

    loader = namespace.get("train_loader")

    assert loader is not None, \
        "Create a variable named train_loader."

    assert isinstance(loader, DataLoader), \
        "train_loader must be a DataLoader."

    assert loader.batch_size == 32, \
        "Use batch_size=32."

    return "Excellent! DataLoader created successfully."