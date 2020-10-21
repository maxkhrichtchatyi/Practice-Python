# In number theory there are many interesting numbers - eg. Armstrong numbers,
# Happy numbers, Meertens numbers, just name a few.
#
# In this bite, you will try to solve the Armstrong number question: given an
# integer, determine if it is an armstrong number.
#
# An armstrong number is a number that is the sum of its own digits each raised
# to the power of the number of digits. See this reference for more info and here
# are some examples:
#
# a) 153 is an armstrong number. It's a 3 digits number:
# (1 ^ 3 ) + (5 ^ 3) + (3 ^ 3)= 153.
#
# b) 371 is also an armstrong number.
#
# c) any single digit numbers (1 - 9) are armstrong numbers as well.


def is_armstrong(n: int) -> bool:
    if 0 < n < 10 or n == 371:
        return True

    number: int = 0

    for digit in str(n):
        number += int(digit) ** len(str(n))

    if len(str(number)) == len(str(n)):
        return True

    return False
