from collections import defaultdict
from itertools import groupby, combinations
import sys
from graphviz import Digraph

from DN40 import Morph, arg_int
from DN41 import Chunk, Sentence

def main():
    sent_id = arg_int() + 1
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            graph = Digraph(format='png')
            graph.attr('node', shape='circle')
            edges = sent.dep_edge()
            print(edge)
            graph.render(f'dep_tree_ai{i}.png')
            break

if __name__ == '__main__':
    main()
