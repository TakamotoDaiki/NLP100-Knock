import torch
from torch import optim
from torch import nn

from my_lib import tokenizer, load_dic, load_dataset
from my_class import CNN, CreateDataset, Padsequence
from my_train import train_model, cal_loss_and_acc
from my_get_weight import get_weight

def main():
    dataset = load_dataset()
    word2id = load_dic()
    emb_weights = get_weight()
    
    vocab_size = len(set(word2id.values())) + 1
    emb_size = 300
    padding_idx = len(set(word2id.values()))
    output_size = 4
    out_channels = 100
    kernel_heights = 3
    stride = 1
    padding = 1

    model = CNN(vocab_size, emb_size, padding_idx, output_size, out_channels,
                kernel_heights, stride, padding, emb_weights=emb_weights)

    for i in range(10):
        x = dataset[0][i]['inputs']
        print(torch.softmax(model(x.unsqueeze(0)), dim=-1))


if __name__ == '__main__':
    main()
