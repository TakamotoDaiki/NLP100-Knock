from gensim.models import KeyedVectors
from pprint import pprint

def main():
    model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

    top10 = model.most_similar('United_States', topn=10)
    pprint(top10)

if __name__ == '__main__':
    main()
