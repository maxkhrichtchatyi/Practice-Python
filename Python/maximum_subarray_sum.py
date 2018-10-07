#!/bin/python3
# -*- coding: utf-8 -*-

"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list
of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


def maxSequence(arr):
    max_sum_end = 0
    max_sum_current = 0

    for number in arr:
        max_sum_current = max_sum_current + number

        if max_sum_current < 0:
            max_sum_current = 0

        if max_sum_end < max_sum_current:
            max_sum_end = max_sum_current

    return max_sum_end

print('Run the "maxSequence" function', end='\n')
print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
