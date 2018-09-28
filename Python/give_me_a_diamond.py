#!/bin/python3
# -*- coding: utf-8 -*-

"""
You need to return a string that displays a diamond shape on the screen using asterisk ("*") characters. Please see
provided test cases for exact output format.

The shape that will be returned from print method resembles a diamond, where the number provided as input represents
the number of *’s printed on the middle line. The line above and below will be centered and will have 2 less *’s than
the middle line. This reduction by 2 *’s for each line continues until a line with a single * is printed at the top
and bottom of the figure.

Return null if input is even number or negative (as it is not possible to print diamond with even number or negative
number).
"""


def diamond(n):
    if n < 3 or n % 2 == 0:
        diamond = None
    else:
        diamond = ''

        for i in range(1, n + 1, 2):
            diamond += ' ' * int((n - i) / 2) + '*' * i + '\n'

        for i in range(n - 2, 0, -2):
            diamond += ' ' * int((n - i) / 2) + '*' * i + '\n'

    return diamond


def diamond_extra(n):
    diamond = None

    if n > 0 and n % 2 == 1:
        diamond = ''
        for i in range(n):
            diamond += ' ' * abs((n / 2) - i)
            diamond += '*' * (n - abs((n - 1) - 2 * i))
            diamond += "\n"

    return diamond


print('Run the "diamond" function', end='\n')
print(diamond(7))

print('Run the "diamond_extra" function', end='\n')
print(diamond(7))
