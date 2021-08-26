import argparse
from itertools import groupby
import sys

class Morph:
    __slots__ = ('surface', 'pos', 'pos1', 'base')

    def __init__(self, line):
        self.surface, temp = line.rstrip().split('\t')
        info = temp.split(',')
        self.pos = info[0]
        self.pos1 = info[1]
        self.base = info[6]

    @classmethod
    def load_cabocha(cls, fi):
        for is_eos, sentence in groupby(fi, key=lambda x: x == 'EOS\n'):
            if not is_eos:
                yield [cls(line) for line in sentence if not line.startswith('* ')]

    def __str__(self):
        return self.surface

    def __repr__(self):
        return 'No.40.Morph({})'.format(', '.join((self.surface, self.pos, self.pos1, self.base)))

def main():
    sent_idx = arg_int() + 1
    for i, sent_lis in enumerate(Morph.load_cabocha(sys.stdin), start=1):
        if i == sent_idx:
            print(repr(sent_lis))
            break

def arg_int():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default='1', type=int)
    args = parser.parse_args()
    return args.number

if __name__ == '__main__':
    main()
