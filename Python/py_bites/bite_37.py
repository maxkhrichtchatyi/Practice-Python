# Although you have to be careful using recursion it is one of those
# concepts you want to at least understand. It's also commonly used
# in coding interviews :)
#
# In this beginner Bite we let you rewrite a simple countdown for
# loop using recursion. See countdown_for below, it produces the
# following output:
#
# $ python countdown.py
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# time is up
#
# You will be tested on having the same output, making it work with
# another start value, and of course if you used recursion. Have fun!

import inspect


def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print("time is up")


def countdown_recursive(start=10):
    while start > 0:
        print(start)
        return countdown_recursive(start - 1)

    print("time is up")


expected = """10
9
8
7
6
5
4
3
2
1
time is up
"""
expected_other_start_arg = """13
12
11
"""
expected_other_start_arg += expected


def test_countdown_for(capfd):
    countdown_for()
    out, _ = capfd.readouterr()
    assert out == expected


def test_countdown_recursive(capfd):
    countdown_recursive()
    out, _ = capfd.readouterr()
    assert out == expected


def test_test_countdown_recursive_different_start(capfd):
    countdown_recursive(13)
    out, _ = capfd.readouterr()
    assert out == expected_other_start_arg


def test_recursion_used():
    func = countdown_recursive
    err = f"expecting {func.__name__} twice in your answer"
    assert inspect.getsource(func).count(func.__name__) == 2, err
