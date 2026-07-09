import torch
import torch.nn as nn


class SimpleCNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(
            3,
            16,
            3,
            padding=1,
        )

        self.pool = nn.MaxPool2d(2)

        self.fc1 = nn.Linear(
            16 * 112 * 112,
            2,
        )

    def forward(self, x):

        x = self.pool(torch.relu(self.conv1(x)))
        x = torch.flatten(x, 1)

        return self.fc1(x)


model = SimpleCNN()

{{USER_CODE}}