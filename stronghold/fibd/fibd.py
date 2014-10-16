# http://rosalind.info/problems/fibd/

from itertools import islice

def solve(n, m):
    if n == 0:
        return 0

    rabbits = [0 for i in xrange(m)]
    rabbits[0] = 1
    for i in xrange(1, n):
        rabbits.insert(0, sum(islice(rabbits, 1, m)))
        rabbits.pop()

    return sum(rabbits)

n, m = map(int, raw_input().split())
print solve(n, m)
