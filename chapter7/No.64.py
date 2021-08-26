from gensim.models import KeyedVectors
from pprint import pprint

def main():
    model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

    with open('questions-words.txt', 'r') as f1, open('ans64.txt', 'w') as f2:
        for line in f1:
            line = line.split()
            if line[0] == ':':
                category = line[1]
            else:
                word, cos = model.most_similar(positive=[line[1], line[2]], negative=[line[0]], topn=1)[0]
                f2.write(' '.join([category] + line + [word, str(cos) + '\n']))
                

if __name__ == '__main__':
    main()
