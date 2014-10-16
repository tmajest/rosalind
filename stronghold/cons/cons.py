# http://rosalind.info/problems/cons/

import sys, collections

def parseFasta(lines):
    dnaStr = []
    for line in lines[1:]:
        if line[0] == ">":
            yield "".join(dnaStr)
            dnaStr = []
        else:
            dnaStr.append(line.rstrip())
    yield "".join(dnaStr)

dnaStrings = list(parseFasta(sys.stdin.readlines()))
print zip(*dnaStrings)


profile = collections.defaultdict(list)
consensus = []

for i in range(len(dnaStrings[0])):
    counter = collections.Counter(s[i] for s in dnaStrings)
    for c in "ACGT":
        profile[c].append(counter[c])
    consensus.append(counter.most_common(1)[0][0])

#print ''.join(consensus)
#for c in "ACGT":
    #print "{0}: {1}".format(c, " ".join(map(str, profile[c])))
