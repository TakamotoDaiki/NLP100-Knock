from itertools import islice
import sys

from load import read_mecab

def main():
    for sent_lis in islice(read_mecab(sys.stdin), 10):
        for word in filter(lambda x: x['pos'] == '動詞', sent_lis):
            print(word['surface'])

if __name__ == '__main__':
    main()
