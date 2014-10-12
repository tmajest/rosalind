# http://rosalind.info/problems/mprt/

import requests
import fasta
import sys
import re

def downloadFasta(pId):
    url = "http://www.uniprot.org/uniprot/{0}.fasta".format(pId)
    return requests.get(url).text

pids = [p.rstrip() for p in sys.stdin.readlines()]
for pId in pids:
    desc, s = next(fasta.parseStr(downloadFasta(pId)))
    matches = [m.start() + 1 for m in re.finditer("(?=N[^P][ST][^P])", s)]
    
    if matches:
        print pId
        print ' '.join(map(str, matches))
