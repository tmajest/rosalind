# http://rosalind.info/problems/iprb/

def prob_AA(k, m, n):
    """
    Returns the probability that any two randomly chosen organisms
    from species k, m, or n will be homozygous dominant.
    """
    total = float(k + m + n)

    # Choose AA then AA gives 100% chance of being AA
    p1 = (k / total) * ((k-1) / (total-1))

    # Choose AA then Aa gives 50% chance of being AA
    p2 = 0.5 * (k / total) * (m / (total-1))

    # Choose Aa then AA gives 50% chance of being AA
    p3 = 0.5 * (m / total) * (k / (total-1))
    
    # Choose Aa then Aa gives 25% chance of being AA
    p4 = 0.25 * (m / total) * ((m-1) / (total-1))

    return p1 + p2 + p3 + p4

def prob_Aa(k, m, n):
    """
    Returns the probability that any two randomly chosen organisms
    from species k, m, or n will be heteroygous
    """
    total = float(k + m + n)

    # Choose AA then Aa gives 50% chance of being Aa
    p1 = 0.5 * (k / total) * (m / (total-1))

    # Choose AA then aa gives 100% chance of being Aa
    p2 = (k / total) * (n / (total-1))

    # Choose Aa then AA gives 50% chance of being Aa
    p3 = 0.5 * (m / total) * (k / (total-1))

    # Choose Aa then Aa gives 50% chance of being Aa
    p4 = 0.5 * (m / total) * ((m-1) / (total-1))

    # Choose Aa then aa gives 50% chance of being Aa
    p5 = 0.5 * (m / total) * (n / (total-1))

    # Choose aa then AA gives 100% chance of being Aa
    p6 = (n / total) * (k / (total-1))

    # Choose aa then Aa gives 50% chance of being Aa
    p7 = 0.5 * (n / total) * (m / (total-1))

    return p1 + p2 + p3 + p4 + p5 + p6 + p7

k, m, n = map(int, raw_input().split(" "))
print prob_AA(k, m, n) + prob_Aa(k, m, n)
