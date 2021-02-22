# Here is a beginner Bite to write Fizz Buzz:
#
# Fizz buzz is a group word game for children to teach them about division.
# Players take turns to count incrementally, replacing any number divisible
# by three with the word "fizz", and any number divisible by five with the
# word "buzz".
# ...
# For example, a typical round of fizz buzz would start as follows:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz,
# 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz,
# 31, 32, Fizz, 34, Buzz, Fizz, ..
#
# Complete the fizzbuzz function below, it should take a number and return the right str or int.

import pytest


def fizzbuzz(num):
    fizz = num % 3 == 0
    buzz = num % 5 == 0

    if fizz and buzz:
        return "Fizz Buzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return num


@pytest.mark.parametrize(
    "arg, ret",
    [
        (1, 1),
        (2, 2),
        (3, "Fizz"),
        (4, 4),
        (5, "Buzz"),
        (6, "Fizz"),
        (7, 7),
        (8, 8),
        (9, "Fizz"),
        (10, "Buzz"),
        (11, 11),
        (12, "Fizz"),
        (13, 13),
        (14, 14),
        (15, "Fizz Buzz"),
        (16, 16),
    ],
)
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret
