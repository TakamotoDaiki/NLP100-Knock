import sys
from itertools import groupby, islice

from load import read_mecab

def main():
    for sent_lis in islice(read_mecab(sys.stdin), 20):
        for key, group in groupby(sent_lis, lambda word: word['pos']):
            words = [word['surface'] for word in group]
            if key == '名詞':
                if(len(words) > 1):
                    print(''.join(words))

if __name__ == '__main__':
    main()
