def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]

    if sum_of_digits > 9 * number_of_digits:
        return [-1]

    possible_largest_number = [0] * number_of_digits

    for digit_index in range(number_of_digits):
        if sum_of_digits >= 9:
            possible_largest_number[digit_index] = 9
            sum_of_digits -= 9
        else:
            possible_largest_number[digit_index] = sum_of_digits

    return possible_largest_number


if __name__ == "__main__":

    sum_of_digits = 20
    number_of_digits = 3

    print(find_largest_number(number_of_digits, sum_of_digits))

    sum_of_digits = 100
    number_of_digits = 2

    print(find_largest_number(number_of_digits, sum_of_digits))
