from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr

def main():
    model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    ws353 = []
    with open('combined.csv', 'r') as f:
        next(f)
        for line in f:
            line = [s.strip() for s in line.split(',')]
            line.append(model.similarity(line[0], line[1]))
            ws353.append(line)

    human = np.array(ws353).T[2]
    w2v = np.array(ws353).T[3]
    correlation, pvalue = spearmanr(human, w2v)

    print(f'スピアマン相関係数: {correlation:.3f}')

if __name__ == '__main__':
    main()
