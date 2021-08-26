import torch
from torch import optim
from torch import nn

from my_lib2 import tokenizer, load_dic, load_dataset
from my_class2 import BERTClass, CreateDataset, Padsequence
from my_train2 import train_model, cal_loss_and_acc

def main():
    dataset = load_dataset()
    word2id = load_dic()

    use_cuda = torch.cuda.is_available()
    device = 'cuda' if use_cuda else 'cpu'
    print(f'Using {device} device')
    
    drop_rate = 0.4
    output_size = 4
    batch_size = 32
    num_epochs = 4
    learning_rate = 2e-5

    model = BERTClass(drop_rate, output_size)

    loss_func = nn.BCEWithLogitsLoss()

    optimizer = torch.optim.AdamW(params=model.parameters(), lr=learning_rate)

    log = train_model(dataset[0], dataset[1], batch_size, model, loss_func,
                      optimizer, num_epochs, device=device)

    #_, acc_train = cal_loss_and_acc(model, dataset[0], device)
    #_, acc_test = cal_loss_and_acc(model, dataset[2], device)
    #print(f'正解率（学習データ）:{acc_train:.3f}')
    #print(f'正解率（評価データ）:{acc_test:.3f}')


if __name__ == '__main__':
    main()
