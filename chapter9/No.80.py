import re
import spacy
import torch
from collections import Counter

nlp = spacy.load('en_core_web_sm', disable=('ner', 'parser'))
categories = ['b', 't', 'e', 'm']
category_names = ['business', 'science and technology', 'entertainment', 'health']

def tokenize(x):
    x = re.sub(r'\s+', ' ', x)
    x = nlp.make_doc(x)
    x = [d.text for d in x]

    return x

def read_feature_dataset(filename):
    with open(filename) as f:
        dataset = f.read().splitlines()
    dataset = [line.split('\t') for line in dataset]
    dataset_x = [tokenize(line[1]) for line in dataset]
    dataset_y = [categories.index(line[0]) for line in dataset]
    return dataset_x, torch.tensor(dataset_y, dtype=torch.long)

def sent_to_ids(sent, vocab_dict):
    ids = torch.tensor([vocab_dict[x if x in vocab_dict else '[UNK]'] for x in sent],
                      dtype=torch.long)
    return ids

def dataset_to_ids(dataset, vocab_dict):
    return [sent_to_ids(x, vocab_dict) for x in dataset]

def main():
    train_x, train_y = read_feature_dataset('train.txt')
    valid_x, valid_y = read_feature_dataset('valid.txt')
    test_x, test_y = read_feature_dataset('test.txt')

    counter = Counter([
        x
        for sent in train_x
        for x in sent
    ])
    vocab_in_train = [
        token
        for token, freq in counter.most_common()
        if freq > 1
    ]
    vocab_list = ['[UNK]'] + vocab_in_train
    vocab_dict = {x:n for n, x in enumerate(vocab_list)}

    print(train_x[0])
    print(sent_to_ids(train_x[0], vocab_dict))

    train_ids = dataset_to_ids(train_x, vocab_dict)
    valid_ids = dataset_to_ids(valid_x, vocab_dict)
    test_ids = dataset_to_ids(test_x, vocab_dict)

if __name__ == '__main__':
    main()
