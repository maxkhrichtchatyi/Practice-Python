"""
In a binary matrix (all elements are 0 and 1), every row is sorted in ascending order (0 to the left of 1).
Find the leftmost column index with a 1 in it.

Example 1:
Input:
[[0, 0, 0, 1],
 [0, 0, 1, 1],
 [0, 1, 1, 1],
 [0, 0, 0, 0]]
Output: 1

Example 2:
Input:
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
Output: -1
"""

binary_matrix = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0]
]

col_index = 0
leftmost_column_index = -1

for row in range(len(binary_matrix)):
    if col_index == 0:
        col_index = len(binary_matrix[row])

    for col in range(col_index - 1, -1, -1):
        if binary_matrix[row][col] == 1:
            col_index -= 1

            if leftmost_column_index == -1:
                leftmost_column_index = col

            if leftmost_column_index > col:
                leftmost_column_index = col

        else:
            break

print(leftmost_column_index)
