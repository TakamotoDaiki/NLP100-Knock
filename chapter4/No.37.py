import sys
from collections import Counter

import matplotlib.pyplot as plt

from load import read_mecab

def main():
    word_freq = Counter()
    for sent_lis in read_mecab(sys.stdin):
        for word in sent_lis:
            if word['surface'] == '猫':
                word_freq.update(x['base'] for x in sent_lis if x['surface'] != '猫')
                break
            
    words, count = zip(*word_freq.most_common(10))
    len_word = range(len(words))

    plt.barh(len_word, count, align='center')
    plt.yticks(len_word, words, fontname='IPAGothic')
    plt.xlabel('frequency')
    plt.ylabel('word')
    plt.title('37. 「猫」と共起頻度の高い上位10語', fontname='IPAGothic')
    plt.savefig('37.png')

if __name__ == '__main__':
    main()
