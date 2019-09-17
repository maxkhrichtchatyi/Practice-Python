"""
Given a sorted array nums, remove the duplicates in-place such
that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    min_number = float('-inf')
    index = 0
    deleted = 0

    for number_index in range(0, len(nums)):
        if nums[number_index - deleted] != min_number:
            min_number = nums[number_index - deleted]
            index += 1
        else:
            del nums[index]
            deleted += 1


def remove_duplicates_extra(nums: List[int]) -> int:
    index = 0

    for number_index in range(0, len(nums)):
        if nums[index] != nums[number_index]:
            index += 1
            nums[index] = nums[number_index]
