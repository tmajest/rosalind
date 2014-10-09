# http://rosalind.info/problems/gc/

import sys

def getGcContent(s):
    return float(sum(1 for c in s if c == 'G' or c == 'C')) / len(s)

def parseInput():
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    sId = lines[0][1:]
    s = []

    for line in lines[1:]:
        if line[0] == '>':
            yield sId, getGcContent(''.join(s))
            sId, s = line[1:], []
        else:
            s.append(line)

    yield sId, getGcContent(''.join(s))

sId, s = max([entry for entry in parseInput()], key=lambda x: x[1])
print sId
print s * 100
