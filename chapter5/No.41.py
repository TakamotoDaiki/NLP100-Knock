from collections import defaultdict
from itertools import groupby, combinations
import sys

from DN40 import Morph, arg_int

class Chunk:
    __slots__ = ('idx', 'dst', 'morphs', 'srcs')

    def __init__(self, line):
        info = line.rstrip().split()
        self.idx = int(info[1])
        self.dst = int(info[2].rstrip('D'))
        self.morphs = []
        self.srcs = []

    def __str__(self):
        return ''.join([morph.surface for morph in self.morphs])

    def __repr__(self):
        return 'No.41.py.Chunk({}, {})'.format(self.idx, self.dst)

    def srcs_append(self, src_idx):
        self.srcs.append(src_idx)

    def morphs_append(self, line):
        self.morphs.append(Morph(line))

    def tostr(self):
        # No.42以降用
        return ''.join([morph.surface for morph in self.morphs if morph.pos != '記号'])

    def contain_pos(self, pos):
        # No.43以降用
        return pos in (morph.pos for morph in self.morphs)

    def replace_np(self, symbol):
        # No.49用
        morph_lis = []
        for pos, morphs in groupby(self.morphs, key=lambda x: x.pos):
            if pos == '名詞':
                for morph in morphs:
                    morph_lis.append(symbol)
                    break
            elif pos != '記号':
                for morph in morphs:
                    morph_lis.append(morph.surface)
        return ''.join(morph_lis)

class Sentence:
    __slots__ = ('chunks', 'idx')

    def __init__(self, sent_lines):
        self.chunks = []

        for line in sent_lines:
            if line.startswith('* '):
                self.chunks.append(Chunk(line))
            else:
                self.chunks[-1].morphs_append(line)

        for chunk in self.chunks:
            if chunk.dst != -1:
                self.chunks[chunk.dst].srcs_append(chunk.idx)

    def __str__(self):
        return ' '.join([morph.surface for chunk in self.chunks for morph in chunk.morphs])

    @classmethod
    def load_cabocha(cls, fi):
        for is_eos, sentence in groupby(fi, key=lambda x: x == 'EOS\n'):
            if not is_eos:
                yield cls(sentence)

    def print_dep_idx(self):
        for chunk in self.chunks:
            print('{}:{} => {}'.format(chunk.idx, chunk, chunk.dst))

    def print_dep(self):
        # No.42用
        for chunk in self.chunks:
            if chunk.dst != -1:
                print('{}\t{}'.format(chunk.tostr(), self.chunks[chunk.dst].tostr()))

    def print_noun_verb_dep(self):
        # No.43用
        for chunk in self.chunks:
            if chunk.contain_pos('名詞') and self.chunks[chunk.dst].contain_pos('動詞'):
                print('{}\t{}'.format(chunk.tostr(), self.chunks[chunk.dst].tostr()))

    def dep_edge(self):
        # No.44用
        return [(f"{i}: {chunk.tostr()}", f"{chunk.dst}: {self.chunks[chunk.dst].tostr()}")
                for i, chunk in enumerate(self.chunks) if chunk.dst != -1]

    def case_pattern(self):
        # No.45用
        for chunk in self.chunks:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    verb = morph.base
                    particles = []
                    for src in chunk.srcs:
                        particles.extend([word.base for word in self.chunks[src].morphs
                                          if word.pos == '助詞'][-1:])
                    particles.sort()
                    print('{}\t{}'.format(verb, ' '.join(particles)))
                    break

    def pred_case_arg(self):
        # No.46用
        for chunk in self.chunks:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    verb = morph.base
                    particle_chunks = []
                    for src in chunk.srcs:
                        particle_chunks.extend([(word.base, self.chunks[src].tostr())
                                                for word in self.chunks[src].morphs if word.pos == '助詞'][-1:])
                    if particle_chunks:
                        particle_chunks.sort()
                        particles, chunks = zip(*particle_chunks)
                    else:
                        particles, chunks = [], []

                    print('{}\t{}\t{}'.format(verb, ' '.join(particles), ' '.join(chunks)))
                    break

    def sahen_case_arg(self):
        # No.47用
        sahen_flag = 0
        for chunk in self.chunks:
            for morph in chunk.morphs:
                if sahen_flag == 0 and morph.pos1 == 'サ変接続':
                    sahen_flag = 1
                    sahen = morph.surface
                elif sahen_flag == 1 and morph.base == 'を' and morph.pos == '助詞':
                    sahen_flag = 2
                elif sahen_flag == 2 and morph.pos == '動詞':
                    sahen_wo = sahen + 'を'
                    verb = morph.base
                    particle_chunks = []
                    for src in chunk.srcs:
                        particle_chunks.extend([(word.base, self.chunks[src].tostr()) for word in self.chunks[src].morphs
                                                if word.pos == '助詞'][-1:])
                    for j, part_chunk in enumerate(particle_chunks[:]):
                        if sahen_wo in part_chunk[1]:
                            del particle_chunks[j]

                    if particle_chunks:
                        particle_chunks.sort()
                        particles, chunks = zip(*particle_chunks)
                    else:
                        particles, chunks = [], []

                    print('{}\t{}\t{}'.format(sahen_wo + verb, ' '.join(particles), ' '.join(chunks)))
                    sahen_flag = 0
                    break
                else:
                    sahen_flag = 0

    def trace_dep_path(self):
        # No.48用
        path = []
        for chunk in self.chunks:
            if chunk.contain_pos('名詞'):
                path.append(chunk)
                d = chunk.dst
                while d != -1:
                    path.append(self.chunks[d])
                    d = self.chunks[d].dst

                yield path
                path = []

    def print_noun2noun_path(self):
        # No.49用
        all_paths = list(self.trace_dep_path())
        arrow = ' -> '
        all_paths_set = [{chunk.idx for chunk in chunks} for chunks in all_paths]
        for p1, p2 in combinations(range(len(all_paths)), 2):
            intersec = all_paths_set[p1] & all_paths_set[p2]
            len_intersec = len(intersec)
            len_smaller = min(len(all_paths_set[p1]), len(all_paths_set[p2]))
            if 0 < len_intersec < len_smaller:
                k = min(intersec)
                path1_lis = []
                path1_lis.append(all_paths[p1][0].replace_np('X'))
                for chunk in all_paths[p1][1:]:
                    if chunk.idx < k:
                        path1_lis.append(chunk.tostr())
                    else:
                        break
                path2_lis = []
                rest_lis = []
                path2_lis.append(all_paths[p2][0].replace_np('Y'))
                for chunk in all_paths[p2][1:]:
                    if chunk.idx < k:
                        path2_lis.append(chunk.tostr())
                    else:
                        rest_lis.append(chunk.tostr())
                print(' | '.join([arrow.join(path1_lis), arrow.join(path2_lis),
                                  arrow.join(rest_lis)]))

        for chunks in all_paths:
            for j in range(1, len(chunks)):
                if chunks[j].contain_pos('名詞'):
                    outstr = []
                    outstr.append(chunks[0].replace_np('X'))
                    outstr.extend(chunk.tostr() for chunk in chunks[1:j])
                    outstr.append(chunks[j].replace_np('Y'))
                    print(arrow.join(outstr))

def main():
    sent_id = arg_int() + 1
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            sent.print_dep_idx()

if __name__ == '__main__':
    main()
