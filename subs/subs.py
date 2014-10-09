# http://rosalind.info/problems/subs/

s, t = raw_input(), raw_input()

p = s.find(t)
while p >= 0:
    print p + 1,
    p = s.find(t, p + 1)
