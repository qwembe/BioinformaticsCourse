from hamDist import hemmingDist

MAX_INT = 1000000


def closestSubstring(seq1, seq2):
    seq1, seq2 = (seq1, seq2) if len(seq1) <= len(seq2) else (seq2, seq1)  # seq1 < seq2
    i, j = 0, len(seq2) - len(seq1)

    res = []
    min_hem = MAX_INT

    while i <= j:  # O(n^2)
        temp = hemmingDist(seq1, seq2[i:i + len(seq1)])
        if min_hem > temp:
            min_hem = temp
            res = [i, seq2[i:i + len(seq1)], min_hem]
        i += 1

    return res
