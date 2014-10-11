# http://rosalind.info/problems/lcsm/

import fasta, collections

strings = [s for desc, s in fasta.parse()]
subs, longest = strings[0], ""

for i in xrange(len(subs)):
    indexes = collections.defaultdict(int)

    for j in xrange(1, len(subs) - i + 1):
        substr = subs[i : i+j]
        if all(substr in s for s in strings):
            longest = max(substr, longest, key=len)
        else:
            break

print longest
