import torch

from my_lib import load_dic, tokenizer, load_dataset
from my_class import RNN

def main():
    dataset = load_dataset()

    print(f'len(Dataset)の出力: {len(dataset[0])}')
    print('Dataset[index]の出力:')
    for var in dataset[0][1]:
        print(f' {var}: {dataset[0][1][var]}')

    word2id = load_dic()

    device = 'cpu'

    vocab_size = len(set(word2id.values())) + 1
    emb_size = 300
    padding_idx = len(set(word2id.values()))
    output_size = 4
    hidden_size = 50
    num_layers = 1

    model = RNN(vocab_size, emb_size, padding_idx, output_size, hidden_size,
                device, num_layers)

    for i in range(10):
        x = dataset[0][i]['inputs']
        print(torch.softmax(model(x.unsqueeze(0)), dim=-1))

if __name__ == '__main__':
    main()
