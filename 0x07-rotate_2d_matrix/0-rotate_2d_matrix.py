#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix: list):
    """ Rotate a 2D matrix
    """
    transpose(matrix)
    n = len(matrix)
    for i in range(n):
        matrix[i] = matrix[i][::-1]


def transpose(matrix: list):
    """ Transpose a 2D matrix in-place
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
