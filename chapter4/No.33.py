from itertools import islice
import sys

from load import read_mecab

def main():
    for sent_lis in islice(read_mecab(sys.stdin), 20):
        for i in range(len(sent_lis) - 2):
            if (sent_lis[i]['pos'] == '名詞' and sent_lis[i+1]['base'] == 'の'
                and sent_lis[i+2]['pos'] == '名詞'):
                print(''.join(x['surface'] for x in sent_lis[i: i+3]))

if __name__ == '__main__':
    main()
