from gensim.models import KeyedVectors

def main():
    model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

    cos_similarity = model.similarity('United_States', 'U.S.')
    print(cos_similarity)

if __name__ == '__main__':
    main()
