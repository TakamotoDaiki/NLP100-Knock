import torch
from torch import nn
from torch.nn import functional as F

from original_lib import load_torch

class Perceptron(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = nn.Linear(input_size, output_size, bias=False)
        torch.manual_seed(0)
        nn.init.normal_(self.fc.weight, 0.0, 1.0)

    def forward(self, x):
        x = self.fc(x)
        return x

def main():
    data = load_torch()

    model = Perceptron(300, 4)

    with torch.no_grad():
        y_hat_1 = F.softmax(model(data[0][:1]), dim=1)
        print(y_hat_1)
        Y_hat = F.softmax(model(data[0][:4]), dim=1)
        print(Y_hat)


if __name__ == '__main__':
    main()
