import sys
from collections import Counter

import matplotlib.pyplot as plt

from load import read_mecab

def main():
    word_freq = Counter(word['base'] for sent_lis in read_mecab(sys.stdin)
                        for word in sent_lis)
    data = Counter(count for count in word_freq.values())

    x, y = data.keys(), data.values()
    

    plt.bar(x, y)
    plt.xlim(1, 30)
    plt.xlabel('frequency')
    plt.ylabel('number of the words')
    plt.title('38. ヒストグラム', fontname='IPAGothic')
    plt.savefig('38.png')

if __name__ == '__main__':
    main()
