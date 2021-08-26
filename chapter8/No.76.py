import torch
from torch.utils.data import TensorDataset, DataLoader
from torch import nn
from torch.utils.tensorboard import SummaryWriter
from original_lib import load_torch
from my_class import Perceptron

def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (x, y) in enumerate(dataloader):
        pred = model(x)
        loss = loss_fn(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 3000 == 0:
            loss, current = loss.item(), batch * len(x)
            print(f'loss: {loss:>7f} [{current:>5d}/{size:>5d}]')

def test_loop(dataloader, model, loss_fn, epoch, writer, mode):
    size = len(dataloader.dataset)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for x, y in dataloader:
            pred = model(x)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= size
    correct /= size
    print(f'Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n')
    if mode == 1:
        writer.add_scalar('Loss/train', test_loss, epoch)
        writer.add_scalar('Accuracy/train', correct, epoch)
    else:
        writer.add_scalar('Loss/valid', test_loss, epoch)
        writer.add_scalar('Accuracy/valid', test_loss, epoch)

def main():
    data = load_torch()
    train_data = TensorDataset(data[0], data[3])
    valid_data = TensorDataset(data[1], data[4])
    test_data = TensorDataset(data[2], data[5])

    train_DL = DataLoader(train_data, batch_size=1, shuffle=True)
    valid_DL = DataLoader(valid_data, batch_size=len(valid_data), shuffle=False)
    test_DL = DataLoader(test_data, batch_size=len(test_data), shuffle=False)

    model = Perceptron(300, 4)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1.0)
    writer = SummaryWriter()

    epochs = 10
    for epoch in range(epochs):
        print(f'Epoch {epoch+1}\n---')
        train_loop(train_DL, model, loss_fn, optimizer)
        checkpoint = {'epoch': epoch, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()}
        torch.save(checkpoint, f'./data/checkpoint_{epoch + 1}.pt')
        mode = 1
        test_loop(train_DL, model, loss_fn, epoch, writer, mode)
        mode = 2
        test_loop(valid_DL, model, loss_fn, epoch, writer, mode)
    print('Done!!!')
    writer.close()

if __name__ == '__main__':
    main()
