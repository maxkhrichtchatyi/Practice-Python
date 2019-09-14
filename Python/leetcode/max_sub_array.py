"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    max_sum = 0

    for number_index in range(1, len(nums)):
        if nums[number_index - 1] > 0:
            nums[number_index] += nums[number_index - 1]

        if nums[number_index] > max_sum:
            max_sum = nums[number_index]

    return max_sum


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
