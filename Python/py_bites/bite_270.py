# Given an integer number, find the most frequent digit in it.
#
# Examples:
#
# 1998 -> two 9's, one 1, one 8 so return 9
# 177 -> return 7
# 2020 -> there is 2 two's, 2 zero's. Return 2 = the first highest hitter
# 12345 -> all digits occur once, so like the last example return the first digit = 1


def freq_digit(num: int) -> int:
    most_frequent_digit: int = 0
    frequents_digit: dict = {}

    for digit in str(num):
        if digit in frequents_digit:
            frequents_digit[digit] += 1
        else:
            frequents_digit[digit] = 1

        if int(frequents_digit.get(digit, 0)) > int(
            frequents_digit.get(str(most_frequent_digit), 0)
        ):
            most_frequent_digit = int(digit)

    return most_frequent_digit
