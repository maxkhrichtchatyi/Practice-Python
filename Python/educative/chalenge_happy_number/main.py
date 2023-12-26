def sum_of_squared_digits(number):
    total_sum = 0

    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit**2

    return total_sum


def is_happy_number(n):
    if n < 1 or n > 2**31:
        return False

    slow = n
    fast = sum_of_squared_digits(n)

    while fast != 1 and fast != slow:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))

    if fast == 1:
        return True

    return False


def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i + 1, ".\tInput Number: ", inputs[i], sep="")
        print("\tIs it a happy number? ", is_happy_number(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()
