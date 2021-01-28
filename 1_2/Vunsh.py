from Bio.SubsMat import MatrixInfo as matlist

matrix = matlist.blosum62

from pprint import pprint

def Wunsch(seq1, seq2, matrix=matrix, gap_cost=1):
    a, b = len(seq1) + 1, len(seq2) + 1

    d = [[0] * a for i in range(b)]

    for i in range(1, b):
        d[i][0] = gap_cost * i

    for j in range(1, a):
        d[0][j] = gap_cost * j

    pprint(matrix)

    for i in range(1, b):
        for j in range(1, a):
            change = d[i - 1][j - 1] + matrix[(seq1[i - 1], seq2[j - 1])]
            delete = d[i][j - 1] + gap_cost
            insert = d[i][j - 1] + gap_cost
            d[i][j] = min(change, delete, insert)

    alignment_a = ""
    alignment_b = ""
    b -= 1
    a -= 1
    i = b
    j = a
    while i > 0 and j > 0:
        score_current = d[i][j]
        score_diagonal = d[i - 1][j - 1]
        score_up = d[i][j - 1]
        score_left = d[i - 1][j]

        if score_current == score_diagonal + matrix[(seq1[j - 1], seq2[i - 1])]:
            alignment_a += seq1[j - 1]
            alignment_b += seq2[i - 1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap_cost:
            alignment_a += seq1[j - 1]
            alignment_b += '-'
            j -= 1
        elif score_current == score_left + gap_cost:
            alignment_a += '-'
            alignment_b += seq2[i - 1]
            i -= 1

    while j > 0:
        alignment_a += seq1[j - 1]
        alignment_b += '-'
        j -= 1
    while i > 0:
        alignment_a += '-'
        alignment_b += seq2[i - 1]
        i -= 1

    alignment_a = alignment_a[::-1]
    alignment_b = alignment_b[::-1]
    return alignment_a, alignment_b, d[b][a]


    # return d[-1][-1]

    # return matrix
