from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

dataset = datasets.ImageFolder(
    "assets/dataset",
    transform=transform,
)

train_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
)