# http://rosalind.info/problems/iev/

lookup = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
populations = map(int, raw_input().split())
print sum(p * 2 * k for p, k in zip(populations, lookup))
