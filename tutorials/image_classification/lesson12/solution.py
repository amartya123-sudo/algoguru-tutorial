import torch
import torch.nn as nn
import torch.optim as optim

from PIL import Image

from torchvision import datasets
from torchvision import transforms

from torch.utils.data import DataLoader


# ==========================
# Image Transform
# ==========================

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    ),
])


# ==========================
# Dataset
# ==========================

dataset = datasets.ImageFolder(
    "assets/dataset",
    transform=transform,
)

train_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
)

class_names = dataset.classes


# ==========================
# CNN Model
# ==========================

class SimpleCNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(
            in_channels=3,
            out_channels=16,
            kernel_size=3,
            padding=1,
        )

        self.pool = nn.MaxPool2d(
            kernel_size=2,
            stride=2,
        )

        self.fc1 = nn.Linear(
            16 * 112 * 112,
            len(class_names),
        )

    def forward(self, x):

        x = self.conv1(x)
        x = torch.relu(x)

        x = self.pool(x)

        x = torch.flatten(x, 1)

        x = self.fc1(x)

        return x


# ==========================
# Training Setup
# ==========================

model = SimpleCNN()

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001,
)


# ==========================
# Training
# ==========================

epochs = 2

for epoch in range(epochs):

    model.train()

    running_loss = 0.0

    for images, labels in train_loader:

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(
            outputs,
            labels,
        )

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    print(
        f"Epoch {epoch + 1}/{epochs} "
        f"Loss: {running_loss / len(train_loader):.4f}"
    )


# ==========================
# Evaluation
# ==========================

model.eval()

correct = 0
total = 0

with torch.no_grad():

    for images, labels in train_loader:

        outputs = model(images)

        _, predicted = torch.max(
            outputs,
            1,
        )

        total += labels.size(0)

        correct += (
            predicted == labels
        ).sum().item()

accuracy = 100 * correct / total

print(f"Accuracy: {accuracy:.2f}%")


# ==========================
# Save Model
# ==========================

torch.save(
    model.state_dict(),
    "model.pth",
)

print("Model saved as model.pth")


# ==========================
# Load Model
# ==========================

loaded_model = SimpleCNN()

loaded_model.load_state_dict(
    torch.load("model.pth")
)

loaded_model.eval()


# ==========================
# Predict One Image
# ==========================

image = Image.open(
    "assets/sample.jpg"
).convert("RGB")

image = transform(image)

image = image.unsqueeze(0)

with torch.no_grad():

    outputs = loaded_model(image)

    _, predicted = torch.max(
        outputs,
        1,
    )

print(
    "Predicted Class:",
    class_names[predicted.item()],
)

print("\nProject completed successfully!")