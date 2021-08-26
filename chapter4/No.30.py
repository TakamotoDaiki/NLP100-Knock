import argparse
from itertools import groupby, islice
from pprint import pprint
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=3)
    args = parser.parse_args()
    for sent_lis in islice(read_mecab(sys.stdin), args.num-1, args.num):
        pprint(sent_lis)

def read_mecab(fi):
    for is_eos, sentence in groupby(fi, lambda line: line.startswith('EOS')):
        if not is_eos:
            yield list(map(line2dic, sentence))

def line2dic(line):
    surface, info = line.rstrip().split('\t')
    col = info.split(',')
    dic = {'surface': surface,
           'pos': col[0],
           'pos1': col[1],
           'base': col[6]}
    return dic

if __name__ == '__main__':
    main()
