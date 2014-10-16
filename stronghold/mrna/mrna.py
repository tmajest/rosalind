# http://rosalind.info/problems/mrna/

import collections

protein = raw_input()
aa_counts = collections.Counter(open('table.txt').read().split()[1::2])
print reduce(lambda aa, total: aa_counts[aa] * total % 1000000, protein, 3)
