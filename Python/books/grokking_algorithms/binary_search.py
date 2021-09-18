from typing import List, Optional

import pytest


def bynary_search(list_of_values: List[int], required_value: int) -> Optional[int]:
    low = 0
    high = len(list_of_values) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_of_values[mid]
        if guess == required_value:
            return guess
        elif guess < required_value:
            low = mid + 1
        else:
            high = mid - 1

    return None


def test_bynary_search_ok():
    list_of_values = [1, 2, 3, 4, 5, 6, 7]
    required_value = 2
    assert bynary_search(list_of_values, required_value) == 2


def test_bynary_search_fail():
    list_of_values = [1, 2, 3, 4, 5, 6, 7]
    required_value = 21
    assert bynary_search(list_of_values, required_value) == None
