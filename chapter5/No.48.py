from collections import defaultdict
from itertools import groupby, combinations
import sys
import pydot

from DN40 import Morph, arg_int
from DN41 import Chunk, Sentence

def main():
    # -n33
    sent_id = arg_int() + 1
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            path_list = sent.trace_dep_path()
            for path in path_list:
                p = ''
                for morph in path:
                    p += str(morph)
                    p += '->'
                print(p[:-2])
            break

if __name__ == '__main__':
    main()
