from torchvision import datasets
from torchvision import transforms

transform = transforms.ToTensor()

dataset = datasets.ImageFolder(
    "assets/dataset",
    transform=transform,
)

print(dataset.classes)
print(len(dataset))