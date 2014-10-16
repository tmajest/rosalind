# http://rosalind.info/problems/hamm/

s, t = raw_input(), raw_input()
print sum(1 for i in xrange(len(s)) if s[i] != t[i])
