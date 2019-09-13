import unittest


def sort_algorithm(A: list):
    """
    Write a bubble sorting implementation
    """
    n = len(A)

    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def is_not_in_descending_order(a):
    """
    Check if the list a is not descending (means "rather ascending")
    """
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


class TestSort(unittest.TestCase):
    def test_simple_cases(self):
        cases = ([1], [], [1, 2], [1, 2, 3, 4, 5],
                 [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
                 list(range(10)), list(range(10, 0, -1)))
        for b in cases:
            a = list(b)
            sort_algorithm(a)
            self.assertCountEqual(a, b)
            self.assertTrue(is_not_in_descending_order(a))


if True:  # __name__ == "__main__":
    unittest.main()
