# http://rosalind.info/problems/dna/

import collections

d = collections.Counter(raw_input())
print d['A'], d['C'], d['G'], d['T']
