from torchvision import datasets
from torchvision import transforms

transform = transforms.ToTensor()

# Choose ONE dataset by uncommenting it.

# dataset = datasets.CIFAR10(
#     root="data",
#     train=True,
#     download=True,
#     transform=transform,
# )

dataset = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=transform,
)

# dataset = datasets.FashionMNIST(
#     root="data",
#     train=True,
#     download=True,
#     transform=transform,
# )

# dataset = datasets.KMNIST(
#     root="data",
#     train=True,
#     download=True,
#     transform=transform,
# )

# dataset = datasets.EMNIST(
#     root="data",
#     split="letters",
#     train=True,
#     download=True,
#     transform=transform,
# )

print(f"Loaded {dataset.__class__.__name__}")
print(f"Number of images: {len(dataset)}")