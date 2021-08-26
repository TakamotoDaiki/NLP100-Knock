import sys
from collections import Counter
from pprint import pprint

from load import read_mecab

def get_freq():
    word_freq = Counter(word['surface'] for sent_lis in read_mecab(sys.stdin)
                        for word in sent_lis)
    return word_freq.most_common(10)

def main():
    ans = get_freq()
    pprint(ans)

if __name__ == '__main__':
    main()
