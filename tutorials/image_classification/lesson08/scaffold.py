import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Create a tiny dummy dataset so the lesson runs quickly.
images = torch.randn(16, 3, 224, 224)
labels = torch.randint(0, 2, (16,))

train_loader = DataLoader(
    TensorDataset(images, labels),
    batch_size=4,
)

class SimpleCNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 112 * 112, 2)

    def forward(self, x):

        x = self.pool(torch.relu(self.conv1(x)))
        x = torch.flatten(x, 1)
        x = self.fc1(x)

        return x


model = SimpleCNN()

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001,
)

{{USER_CODE}}