"""
Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions.
"""


def get_fib(position: int) -> int:
    if position <= 0:
        return 0
    elif position == 1:
        return 1

    return get_fib(position - 2) + get_fib(position - 1)


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
print(get_fib(8))
print(get_fib(3))
