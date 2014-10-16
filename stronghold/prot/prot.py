# http://rosalind.info/problems/prot/

def constructCodonDictionary(tableFileName):
    table = dict()
    for line in open(tableFileName):
        s = line.rstrip().split()
        for i in range(0, len(s), 2):
            table[s[i]] = s[i+1]
    return table


codonTable = constructCodonDictionary("table.txt")
rnaString, encoded = raw_input(), []

for i in range(0, len(rnaString), 3):
    lookup = codonTable[rnaString[i:i+3]]
    if lookup.upper() != 'STOP':
        encoded.append(lookup)

print ''.join(encoded)
