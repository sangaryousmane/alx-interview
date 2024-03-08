#!/usr/bin/python3
""" This module solves the pascal triangle problem
"""

def pascal_triangle(n):
    """
    Generates the Pascal's triangle up to the specified number of rows.

    :param
      n: The number of rows for which to generate the Pascal's triangle.
    :return:
      A 2D list representing the Pascal's triangle with 'n' rows.
    """
    triangle = [[1]]
    if n <= 0:
        return []

    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return triangle
