# Write a function that can sum up numbers:
#
# It should receive a sequence of n numbers.
# If no argument is provided, return sum of numbers 1..100.
# Look closely to the type of the function's default argument ...


def sum_numbers(numbers=None):
    sum_of_numbers: int = 0

    if numbers is None:
        numbers = range(0, 101)

    for number in numbers:
        sum_of_numbers += number

    return sum_of_numbers
