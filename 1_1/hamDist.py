def hemmingDist(seq1, seq2):
    dist = 0
    n = min(len(seq1), len(seq2))
    for i in range(n):
        if seq1[i] != seq2[i]:
            dist += 1

    return dist


