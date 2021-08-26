import torch
from torch import optim
from torch import nn

from my_lib import tokenizer, load_dic, load_dataset
from my_class import RNN, CreateDataset
from my_train import train_model, cal_loss_and_acc

def main():
    dataset = load_dataset()
    word2id = load_dic()

    device = 'cpu'
    
    vocab_size = len(set(word2id.values())) + 1
    emb_size = 300
    padding_idx = len(set(word2id.values()))
    output_size = 4
    hidden_size = 50
    num_layer = 1
    learning_rate = 1e-3
    batch_size = 1
    num_epochs = 10

    model = RNN(vocab_size, emb_size, padding_idx, output_size, hidden_size,
                device, num_layer)

    loss_func = nn.CrossEntropyLoss()

    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    log = train_model(dataset[0], dataset[1], batch_size, model, loss_func, optimizer, num_epochs)

    _, acc_train = cal_loss_and_acc(model, dataset[0])
    _, acc_test = cal_loss_and_acc(model, dataset[2])
    print(f'正解率（学習データ）:{acc_train:.3f}')
    print(f'正解率（評価データ）:{acc_test:.3f}')

if __name__ == '__main__':
    main()
