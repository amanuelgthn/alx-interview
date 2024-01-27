#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix) - 1):
            matrix[j + 1][i], matrix[i][j + 1] =\
                matrix[i][j + 1], matrix[j + 1][i]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix) // 2):
            matrix[i][j], matrix[i][len(matrix) - j - 1] =\
                matrix[i][len(matrix) - j - 1],  matrix[i][j]
