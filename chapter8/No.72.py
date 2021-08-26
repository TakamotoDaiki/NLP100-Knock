import torch
from torch import nn
from torch.nn import functional as F
from original_lib import load_torch
from my_class import Perceptron

def main():
    data = load_torch()
    loss_fn = nn.CrossEntropyLoss()
    model = Perceptron(300, 4)

    loss1 = loss_fn(model(data[0][:1]), data[3][:1])
    model.zero_grad()
    loss1.backward()

    print('損失(1)：', loss1)
    print('勾配(1)：')
    print(model.fc.weight.grad)

    loss_fn = nn.CrossEntropyLoss()
    loss2= loss_fn(model(data[0][:4]), data[3][:4])
    model.zero_grad()
    loss2.backward()

    print('損失(1-4)：', loss2)
    print('勾配(1-4)：')
    print(model.fc.weight.grad)

    with torch.no_grad():
        y_hat1 = F.softmax(model(data[0][:1]), dim=1)
        print('勾配(W)：')
        print((y_hat1 - torch.tensor([1,0,0,0])).T.matmul(data[0][:1]))

if __name__ == '__main__':
    main()
