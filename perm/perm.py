# http://rosalind.info/problems/perm/

import itertools

n = int(raw_input())
perms = list(itertools.permutations(range(1, n+1)))

print len(perms)
for perm in perms:
    print ' '.join(map(str, perm))
