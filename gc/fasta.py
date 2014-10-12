# Functions for parsing FASTA files

import sys

def _parseHelper(fastaInput):
    """
    Helper function to parse FASTA format.
    """

    desc, sequence = "", []

    for rline in fastaInput:
        line = rline.rstrip()
        if not line:
            break
        elif line[0] == ">":
            if sequence: 
                yield desc, ''.join(sequence)
                sequence = []
            desc = line[1:]
        else:
            sequence.append(line)

    if desc and sequence:
        yield desc, ''.join(sequence)

def parse(f=None):
    """
    Takes a file or stdin of FASTA format and returns a 
    generator of tuples of the form (description, sequence).
    """

    f = f if f else sys.stdin
    return _parseHelper(f)

def parseStr(s):
    """
    Takes a string in FASTA format and returns a generator
    of tuples of the form (description, sequence).
    """

    return _parseHelper(s.split("\n"))
