# In this Bite you are presented with a function that copies the given
# items data structure.
# There is a problem though, the tests fail. Can you fix it?
# This can be done in a one liner. If you know which module to use
# it will be easy, if not you will learn something new today.
# Regardless we want you to think about Python's mutability. Have fun!

from copy import deepcopy
import unittest

items = [
    {"id": 1, "name": "laptop", "value": 1000},
    {"id": 2, "name": "chair", "value": 300},
    {"id": 3, "name": "book", "value": 20},
]


def duplicate_items(items):
    return deepcopy(items[:])


class Test(unittest.TestCase):
    def test_change_copy_only(self):
        items_copy = duplicate_items(items)
        assert items == items_copy

        # modify the copy
        items_copy[0]["name"] = "macbook"
        items_copy[1]["id"] = 4
        items_copy[2]["value"] = 30

        # only copy should have been updated, check original items values
        assert items[0]["name"] == "laptop"
        assert items[1]["id"] == 2
        assert items[2]["value"] == 20


if __name__ == "__main__":
    unittest.main()
