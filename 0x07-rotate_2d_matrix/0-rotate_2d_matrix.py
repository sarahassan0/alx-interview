#!/usr/bin/python3
""" rotate_2d_matrix problem """


def rotate_2d_matrix(matrix):
    """ n x n 2D matrix, rotate it 90 degrees clockwise """

    # Transpose the matrix by swap matrix[r][c] with elements in matrix[c][r]
    for r in range(len(matrix)):
        for c in range(r, len(matrix)):
            if r != c:
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # Revese each row after transpose the given matrix.
    for row in matrix:
        row.reverse()

# More concise solution
    # matrix[::] = [list(i) for i in zip(*matrix[::-1])]
