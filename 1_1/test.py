from Bio import SeqIO
from pprint import pprint

from hamDist import hemmingDist
from subSeq import closestSubstring
from Levenstein import LevDist
from Levenstein import LevDist2

# input = "data/gattaca.fasta"
input = "data/f8.fasta"
# input = "data/GATTACA2.fasta"

seq = []

with open(input, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        seq.append(record.seq)

seq1, seq2 = seq[0], seq[1]
# seq1, seq2 = "POLYNOMIAL", "EXPONENTIAL"
# seq1, seq2 = "H", "AAAAA"

print((seq1, seq2))

# Task 1
# print(hemmingDist(seq1, seq2))

# Task 2
# print(closestSubstring(seq1, seq2))

# Task 3
pprint(LevDist(seq1, seq2))
pprint(LevDist2(seq1, seq2))
