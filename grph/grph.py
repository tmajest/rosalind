# http://rosalind.info/problems/grph/

import fasta

def isConnected(s, t, k):
    """ 
    Returns true if string s has a suffix of length k equal 
    to the prefix of t of length k.
    """
    return s[-k:] == t[:k]

entries = list(fasta.parse())
edges = ((a, b) for i, a in enumerate(entries)
                  for j, b in enumerate(entries)
                    if a != b and isConnected(a[1], b[1], k))

for v1, v2 in edges:
    print v1[0], v2[0]
