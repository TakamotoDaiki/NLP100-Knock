import torch
from torch import optim
from torch import nn

from my_lib import tokenizer, load_dic, load_dataset
from my_class import RNN, CreateDataset, Padsequence
from my_train import train_model, cal_loss_and_acc

def main():
    dataset = load_dataset()
    word2id = load_dic()

    use_cuda = torch.cuda.is_available()
    device = 'cuda' if use_cuda else 'cpu'
    print(f'Using {device} device')
    
    vocab_size = len(set(word2id.values())) + 1
    emb_size = 300
    padding_idx = len(set(word2id.values()))
    output_size = 4
    hidden_size = 50
    num_layers = 1
    learning_rate = 5e-2
    batch_size = 32
    num_epochs = 10

    model = RNN(vocab_size, emb_size, padding_idx, output_size, hidden_size,
                device, num_layers)

    loss_func = nn.CrossEntropyLoss()

    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    log = train_model(dataset[0], dataset[1], batch_size, model, loss_func,
                      optimizer, num_epochs,
                      collate_fn=Padsequence(padding_idx), device=device,
                      use_cuda=use_cuda)

    _, acc_train = cal_loss_and_acc(model, dataset[0], device,
                                    use_cuda=use_cuda)
    _, acc_test = cal_loss_and_acc(model, dataset[2], device,
                                   use_cuda=use_cuda)
    print(f'正解率（学習データ）:{acc_train:.3f}')
    print(f'正解率（評価データ）:{acc_test:.3f}')

if __name__ == '__main__':
    main()
