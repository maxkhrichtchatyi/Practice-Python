"""
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.

Note that the target sum has to be obtained by summing two different integers
in the array; you can't add a single integer to itself in order to obtain the
target sum.

You can assume that there will be at most one pair of numbers summing up to
the target sum.

Simple Input:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Simple Output:
[-1, 11] // the numbers could be in reverse order
"""
def twoNumberSum(array, targetSum):

    array.sort()  # TC O(n*lon(n))
    left = 0
    right = len(array) - 1
    
    while left < right:  # TC O(n)
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return [array[left], array[right]]
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1

    return []

# Total: TC O(n*log(n)), SC O(1)