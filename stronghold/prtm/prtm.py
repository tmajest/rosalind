# http://rosalind.info/problems/prtm/

protein = raw_input()

lines = (line.rstrip().split() for line in open('table.txt').readlines())
table = dict(((k, float(v)) for k, v in lines))

print sum(table[aa] for aa in protein)
