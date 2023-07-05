#!/usr/bin/python3
"""
This module contains the function find_peak(list_of_integers)
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)

    if n == 1:
        return list_of_integers[0]

    if n == 2:
        return max(list_of_integers)

    mid = n // 2

    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])

    return list_of_integers[mid]
