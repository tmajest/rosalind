# http://rosalind.info/problems/orf/

import fasta
import string

def build_dna_table():
    f = open("table.txt").read().split()
    return dict(zip(f[0::2], f[1::2]))

def dna_to_proteins(dna, dna_table):
    codons = [dna[i : i+3] for i in xrange(0, len(dna) - 2, 3)]

    for i, codon in enumerate(codons):
        if codon == "ATG":
            protein = ["M"]
            for codon2 in codons[i+1:]:
                if codon2 in ("TAA", "TAG", "TGA"):
                    yield ''.join(protein)
                    break
                else:
                    protein.append(dna_table[codon2])

dna_table = build_dna_table()
dna = next(fasta.parse())[1]
complement = dna[::-1].translate(string.maketrans("ATCG", "TAGC"))
reading_frames = [dna[i:] for i in xrange(3)] + [complement[i:] for i in xrange(3)]

proteins = set()
for reading_frame in reading_frames:
    for protein in dna_to_proteins(reading_frame, dna_table):
        if protein:
            proteins.add(protein)

print "\n".join(proteins)
