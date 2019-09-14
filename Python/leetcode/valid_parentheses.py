"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
---
Input: "()"
Output: true

Example 2:
---
Input: "()[]{}"
Output: true

Example 3:
---
Input: "(]"
Output: false

Example 4:
---
Input: "([)]"
Output: false

Example 5:
---
Input: "{[]}"
Output: true
"""


def is_valid(s: str) -> bool:
    stack = []
    characters = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for char in s:
        if char in characters:
            stack.append(characters[char])
            continue

        if not len(stack) or char != stack.pop():
            return False

    if len(stack):
        return False

    return True


print(is_valid('()[()({})]'))
