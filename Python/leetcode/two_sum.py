"""
Given an array of integers, return indices of the
two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    numbers_hash = {}

    for number in nums:
        if number in numbers_hash:
            numbers_hash[number] += 1
        else:
            numbers_hash[number] = 1

    i = 0
    result = []

    for number in nums:
        targett = target - number
        if targett in numbers_hash:
            if targett == number and numbers_hash[targett] == 1:
                pass
            else:
                result.append(i)

        i += 1

    return (result)


def two_sum_solution_two(nums: List[int], target: int) -> List[int]:
    numbers_hash = {}
    index = 0
    result = []

    for number in nums:
        complement = target - number

        if complement in numbers_hash:
            result = [numbers_hash[complement], index]
            break

        numbers_hash[number] = index
        index += 1

    return result
