def LevDist(seq1, seq2):
    a, b = len(seq1) + 1, len(seq2) + 1

    d = [[0] * a for i in range(b)]

    for i in range(1, b):
        d[i][0] = d[i - 1][0] + 1

    for j in range(1, a):
        d[0][j] = d[0][j - 1] + 1

    for i in range(1, b):
        for j in range(1, a):
            if seq1[j - 1] != seq2[i - 1]:
                d[i][j] = min(d[i - 1][j] + 1, d[i - 1][j - 1] + 1, d[i][j - 1] + 1)
            else:
                d[i][j] = d[i - 1][j - 1]

    return d[-1][-1]


def LevDist2(seq1, seq2):  # Vagner-Fisher
    seq1, seq2 = (seq1, seq2) if len(seq1) <= len(seq2) else (seq2, seq1)  # seq1 < seq2

    a, b = len(seq1) + 1, len(seq2) + 1
    l = 2                   # Compression
    d = [[0] * a for i in range(l)]

    for i in range(1, l):
        d[i][0] = d[i - 1][0] + 1

    for j in range(1, a):
        d[0][j] = d[0][j - 1] + 1

    for i in range(1, b):
        for j in range(1, a):
            k = i % l  # module focus
            _k = (i - 1) % l
            if seq1[j - 1] != seq2[i - 1]:
                d[k][j] = min(d[_k][j] + 1, d[_k][j - 1] + 1, d[k][j - 1] + 1)
            else:
                d[k][j] = d[_k][j - 1]
        d[k][0] = i
    return d[i % l][-1]
