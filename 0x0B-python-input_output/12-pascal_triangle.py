#!/usr/bin/python3
"""A Pascal Triangle Module
"""


def pascal_triangle(n):
    """A function that displays
    a pascal rectangle
    """

    new_result = []
    me = []
    if n <= 0:
        return (result)
    for i in range(n):
        if i == 0:
            me.append(1)
            new_result.append(me)
        elif i == 1:
            me = me + [1]
            new_result.append(me)
        else:
            new = []
            new.append(me[0])
            for j in range(len(me) - 1):
                sum = 0
                sum = me[j] + me[j + 1]
                new.append(sum)
            new.append(me[-1])
            me = new
            new_result.append(me)
    return (new_result)
