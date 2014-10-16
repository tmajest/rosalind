# http://rosalind.info/problems/1a/

import collections

text, k = raw_input(), int(raw_input())
kmers = (text[i:i+k] for i in xrange(len(text) - k + 1))
counts = collections.Counter(kmers)
max_count = max(counts.values())

print ' '.join(s for s, count in counts.most_common() if count == max_count)
