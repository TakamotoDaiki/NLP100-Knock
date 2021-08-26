import sys
from collections import Counter

import matplotlib.pyplot as plt

from load import read_mecab

def main():
    word_freq = Counter(word['base'] for sent_lis in read_mecab(sys.stdin)
                        for word in sent_lis)
    _, count = zip(*word_freq.most_common())

    plt.plot(range(1, len(count)+1), count)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('log(rank)')
    plt.ylabel('log(frequency)')
    plt.title('39. Zipsの法則', fontname='IPAGothic')
    plt.savefig('39.png')

if __name__ == '__main__':
    main()
