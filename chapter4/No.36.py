import sys
from collections import Counter

import matplotlib.pyplot as plt

from load import read_mecab

def main():
    word_freq = Counter(word['base'] for sent_lis in read_mecab(sys.stdin)
                        for word in sent_lis)
    word, count = zip(*word_freq.most_common(10))
    len_word = range(len(word))

    plt.barh(len_word, count, align='center')
    plt.yticks(len_word, word, fontname = 'IPAGothic')
    plt.xlabel('frequency')
    plt.ylabel('word')
    plt.title('36. 頻度上位10語', fontname = 'IPAGothic')
    plt.savefig('36.png')

if __name__ == '__main__':
    main()
