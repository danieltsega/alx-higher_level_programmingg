#!/usr/bin/python3
"""A Pascal Triangle Module
"""


def pascal_triangle(n):
    """A function that displays
    a pascal rectangle
    """

    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        t_row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                element = 1

            else:
                prev_row = triangle[i - 1]
                left_elem = prev_row[j - 1]
                right_elem = prev_row[j]
                element = left_elem + right_elem

            t_row.append(element)

        triangle.append(t_row)

    return triangle
