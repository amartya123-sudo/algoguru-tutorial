def validate(namespace):

    required = [
        "model",
        "train_loader",
        "criterion",
        "optimizer",
    ]

    missing = [
        name
        for name in required
        if name not in namespace
    ]

    assert not missing, (
        "Missing required objects: "
        + ", ".join(missing)
    )

    return (
        "Congratulations! "
        "You completed the image classification project."
    )