# Martin is preparing to pass an IQ test.
#
# The most frequent task in this test is to find out which one of the
# given characters differs from the others. He observed that one char
# usually differs from the others in being alphanumeric or not.
#
# Please help Martin! To check his answers, he needs a program to find
# the different one (the alphanumeric among non-alphanumerics or vice versa)
# among the given characters.
#
# Complete get_index_different_char to meet this goal. It receives a chars
# list and returns an int index (zero-based).
#
# Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
#
# Examples:
#
# ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
# ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)

import pytest


def get_index_different_char(chars):
    alphanumeric = []
    not_alphanumeric = []

    for position, char in enumerate(chars):
        if str(char).isalnum():
            alphanumeric.append(position)
        else:
            not_alphanumeric.append(position)

    return (
        not_alphanumeric[0]
        if len(alphanumeric) > len(not_alphanumeric)
        else alphanumeric[0]
    )


@pytest.mark.parametrize(
    "arg, expected",
    [
        (["A", "f", ".", "Q", 2], 2),
        ([".", "{", " ^", "%", "a"], 4),
        ([1, "=", 3, 4, 5, "A", "b", "a", "b", "c"], 1),
        (["=", "=", "", "/", "/", 9, ":", ";", "?", "¡"], 5),
        (list(range(1, 9)) + ["}"] + list("abcde"), 8),
        ([2, ".", ",", "!"], 0),
    ],
)
def test_wrong_char(arg, expected):
    error = f"get_index_different_char({arg}) should " f"return index {expected}"
    assert get_index_different_char(arg) == expected, error
