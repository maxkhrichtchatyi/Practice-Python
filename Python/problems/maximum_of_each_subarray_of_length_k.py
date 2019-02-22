"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""

list_of_numbers = [10, 5, 2, 7, 8, 7]
k = 3

for number_position in range(0, len(list_of_numbers) - k + 1):
    max_number_from_subset = 0

    for subset_number_position in range(number_position, number_position + k):
        if list_of_numbers[subset_number_position] > max_number_from_subset:
            max_number_from_subset = list_of_numbers[subset_number_position]

    print(max_number_from_subset)
