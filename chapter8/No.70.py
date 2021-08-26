import spacy
nlp = spacy.load('en_core_web_sm', disable=('ner', 'parser'))

import torch
from original_lib import g_tvt, wv
word_vectors = wv()

def get_textvec(text):
    doc = nlp(text)
    vecs = [word_vectors[token.text] for token in doc if token.text in word_vectors]
    return sum(vecs) / len(vecs)

def main():
    train, valid, test = g_tvt()
    
    x_train = torch.tensor([get_textvec(title) for title in train['TITLE']])
    x_valid = torch.tensor([get_textvec(title) for title in valid['TITLE']])
    x_test = torch.tensor([get_textvec(title) for title in test['TITLE']])
    
    category_dic = {'b': 0, 't': 1, 'e': 2, 'm': 3}
    y_train = torch.tensor(train['CATEGORY'].map(category_dic).values)
    y_valid = torch.tensor(valid['CATEGORY'].map(category_dic).values)
    y_test = torch.tensor(test['CATEGORY'].map(category_dic).values)

    torch.save(x_train, 'x_train.pt')
    torch.save(x_valid, 'x_valid.pt')
    torch.save(x_test, 'x_test.pt')
    torch.save(y_train, 'y_train.pt')
    torch.save(y_valid, 'y_valid.pt')
    torch.save(y_test, 'y_test.pt')

if __name__ == '__main__':
    main()
