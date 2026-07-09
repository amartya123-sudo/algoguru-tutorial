from torchvision import datasets
from torchvision import transforms

transform = transforms.ToTensor()

dataset = datasets.ImageFolder(
    "assets/dataset",
    transform=transform,
)

# Print the class names

# Print the total number of images