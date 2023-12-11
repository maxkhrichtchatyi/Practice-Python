def is_palindrome(s):

    left_pointer = 0
    right_pointer = len(s) - 1

    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False

        left_pointer += 1
        right_pointer -= 1

    return True


if __name__ == "__main__":

    words = ["hello", "kayak", "RACEACAR", "A", "ABCDABCD"]

    for word in words:
        polindrome_status = "is" if is_palindrome(word) else "isn't"
        print(f"{word} {polindrome_status} palindrome")
