"""
Find all the subsequences of length. While doing so compute the sum and of the two elements
and check if it is equal to k. If ye, print Yes, else keep searching. This is a brute Force
approach.

Sort the array in non-decreasing order. Then start traversing the array from its right end.
Say we have the sorted array, {3,5,7,10} and we want the sum to be 17. We will start from
element 10, index=3, let's denote the index with 'j'. Then include the current element and
compute required_sum= sum - current_element. After that, we can perform a binary or ternary
search in array[0- (j-1)] to find if there is an element whose value is equal to the
required_sum. If we find such an element, we can break as we have found a subsequence of
length 2 whose sum is the given sum. If we don't find any such element, then decrease the
index of j and repeat the above-mentioned steps for resulting subarray of length= length-1 i.e.
by excluding the element at index 3 in this case.
"""


def two_numbers_add_up_to_k(numbers: list, k: int) -> str:
    hash_table = {}

    for number in numbers:
        required_number = k - number

        if required_number in hash_table:
            return 'Yes!'

        if number not in hash_table:
            hash_table[number] = 0

    return 'No'


print(two_numbers_add_up_to_k(numbers=[3, 2, 2, 10], k=13