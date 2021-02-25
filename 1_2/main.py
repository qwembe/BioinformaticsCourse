from Vunsh import *
import Bio.Align.substitution_matrices as substitution_matrices

MATRIX = substitution_matrices.load("BLOSUM62")

fr = Wunsch("AGC", "A",MATRIX)
print(fr)

