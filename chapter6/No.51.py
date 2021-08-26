import argparse
import json

from sklearn.feature_extraction.text import CountVectorizer

def ngram_gen(seq, n):
    return zip(*(seq[i:] for i in range(n)))

def make_feats_dict(title):
    nlp = CountVectorizer().build_tokenizer()
    words = nlp(title)

    feats = {}
    for token in words:
        feats[token] = 1.0
    for bigram in ngram_gen(words, 2):
        feats[' '.join(bigram)] = 1.0
    for trigram in ngram_gen(words, 3):
        feats[' '.join(trigram)] = 1.0
    return feats

def dump_features(input_file, output_file):
    with open(input_file) as fi, open(output_file, 'w') as fo:
        for line in fi:
            vals = line.rstrip().split('\t')
            label, title = vals
            feats = {'**LABEL**': label}
            feats.update(make_feats_dict(title))
            print(json.dumps(feats), file=fo)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = vars(parser.parse_args())
    dump_features(**args)

if __name__ == '__main__':
    main()
