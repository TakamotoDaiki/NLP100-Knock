from gensim.models import KeyedVectors
from pprint import pprint

def main():
    model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

    vec = model['Spain'] - model['Madrid'] + model['Athens']
    print(vec)
    top10 = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
    pprint(top10)

if __name__ == '__main__':
    main()
