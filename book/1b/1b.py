# http://rosalind.info/problems/1b/

import string

print raw_input()[::-1].translate(string.maketrans("ATCG", "TAGC"))
