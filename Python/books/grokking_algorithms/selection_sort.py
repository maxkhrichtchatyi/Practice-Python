from typing import List

import pytest


def find_smallest_index(list_of_values: List[int]) -> int:
    smallest = list_of_values[0]
    smallest_index = 0

    for index in range(1, len(list_of_values)):
        if list_of_values[index] < smallest:
            smallest = list_of_values[index]
            smallest_index = index

    return smallest_index


def selection_sort(list_of_values: List[int]) -> int:
    sorted_items = []
    for _ in range(len(list_of_values)):
        smallest_index = find_smallest_index(list_of_values)
        sorted_items.append(list_of_values.pop(smallest_index))
    return sorted_items


def test_find_smallest_index_ok():
    list_of_values = [6, 1, 5, 2, 4, 3]
    assert find_smallest_index(list_of_values) == 1


def test_selection_sort_ok():
    list_of_values = [6, 1, 5, 2, 4, 3]
    assert selection_sort(list_of_values) == [1, 2, 3, 4, 5, 6]
