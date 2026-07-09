def validate(namespace):

    errors = []

    if "torch" not in namespace:
        errors.append("Import the torch library.")

    if "transforms" not in namespace:
        errors.append("Import torchvision.transforms as transforms.")

    if "plt" not in namespace:
        errors.append("Import matplotlib.pyplot as plt.")

    return {
        "success": len(errors) == 0,
        "message": (
            "Great job!"
            if not errors
            else "Some imports are missing."
        ),
        "errors": errors,
    }