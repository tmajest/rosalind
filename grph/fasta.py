import sys

def parse(f=None):
    """
    Takes a file of FASTA format and returns a generator
    of tuples of the form (description, sequence).
    """
    f = f if f else sys.stdin
    desc, sequence = "", []

    for rline in f:
        line = rline.rstrip()
        if line[0] == ">":
            if sequence: 
                yield desc, ''.join(sequence)
                sequence = []
            desc = line[1:]
        else:
            sequence.append(line)

    yield desc, ''.join(sequence)
