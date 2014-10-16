# http://rosalind.info/problems/revc/

print raw_input()[::-1]    \
    .replace("A", "t")     \
    .replace("T", "a")     \
    .replace("C", "g")     \
    .replace("G", "c")     \
    .upper()
