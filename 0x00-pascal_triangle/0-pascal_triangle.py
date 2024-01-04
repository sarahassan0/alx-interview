#!/usr/bin/python3

""" pascal_triangle """


def pascal_triangle(n):
    """Generate the nth row of Pascal's triangle."""

    if n <= 0:
        return []

    triangle = [[1]]
    for r in range(n-1):
        temp = [0] + triangle[-1] + [0]
        new_row = []
        for j in range(len(triangle[-1]) + 1):
            new_row.append(temp[j] + temp[j+1])
        triangle.append(new_row)

    return triangle
