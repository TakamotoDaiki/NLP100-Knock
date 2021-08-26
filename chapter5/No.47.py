from collections import defaultdict
from itertools import groupby, combinations
import sys
import pydot

from DN40 import Morph, arg_int
from DN41 import Chunk, Sentence

def main():
    # -n12
    sent_id = arg_int() + 1
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            sent.sahen_case_arg()
            break

if __name__ == '__main__':
    main()
