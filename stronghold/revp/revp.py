# http://rosalind.info/problems/revp/

import string
import fasta

def reverse_complement(dna):
    return dna[::-1].translate(string.maketrans("ATCG", "TAGC"))

def solve(dna):
    for j in xrange(4, 13):
        for i in xrange(len(dna) - j + 1):
            dna_substring = dna[i:i+j]
            if dna_substring == reverse_complement(dna_substring):
                print i+1, len(dna_substring)

dna = next(fasta.parse())[1]
solve(dna)
