"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they 
add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    numbers_hash = {}  # SC O(n)

    for number in nums:  # TC O(n)
        if number in numbers_hash:
            numbers_hash[number] += 1
        else:
            numbers_hash[number] = 1

    i = 0
    result = []

    for number in nums:  # TC O(n)
        targett = target - number
        if targett in numbers_hash:
            if targett == number and numbers_hash[targett] == 1:
                pass
            else:
                result.append(i)

        i += 1

    return result

# Total: TC O(n+n)=O(2n)=O(n), SC O(n)


def two_sum_solution_two(nums: List[int], target: int) -> List[int]:
    numbers_hash = {}  # SC O(n)
    result = []

    for number_index, number in enumerate(nums):  # TC O(n)
        complement = target - number

        if complement in numbers_hash:
            result = [numbers_hash[complement], number_index]
            break

        numbers_hash[number] = number_index

    return result

# Total: TC O(n), SC O(n)
