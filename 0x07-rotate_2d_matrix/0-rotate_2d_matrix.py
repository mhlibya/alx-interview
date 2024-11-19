#!/usr/bin/python3
"""
0x07-rotate_2d_matrix
"""
def rotate_2d_matrix(matrix):
    n = len(matrix) - 1
    r = (n + 1) // 2 if n % 2 != 0 else n // 2

    for i in range(r):
        top = matrix[i][i : n + 1 - i]
        right = [matrix[j][n - i] for j in range(i, n + 1 - i)]
        bottom = matrix[n - i][i : n + 1 - i][::-1]
        left = [matrix[k][i] for k in range(i, n + 1 - i)][::-1]

        for j in range(i, n + 1 - i):
            matrix[i][j] = left.pop(0)
            matrix[j][n - i] = top.pop(0)
            matrix[n - i][n - j] = right.pop(0)
            matrix[n - j][i] = bottom.pop(0)
