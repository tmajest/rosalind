# http://rosalind.info/problems/gc/

import fasta

def gcContent(s):
    return float(sum(1 for c in s if c == 'G' or c == 'C')) / len(s)

entries = fasta.parse()
contents = ((d, gcContent(s)) for d, s in entries)
desc, maxGcContent = max(contents, key=lambda x: x[1])

print desc 
print maxGcContent * 100
