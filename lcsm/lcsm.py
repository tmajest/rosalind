# http://rosalind.info/problems/lcsm/

import fasta, collections

strings = [s for desc, s in fasta.parse()]
subs = strings[0]
found = []

for i in xrange(len(subs)):
    indexes = collections.defaultdict(int)

    for j in xrange(1, len(subs) - i + 1):
        substr = subs[i : i+j]
        if all(substr in s for s in strings):
            found.append(substr)
        else:
            break

print max(found, key=len)
