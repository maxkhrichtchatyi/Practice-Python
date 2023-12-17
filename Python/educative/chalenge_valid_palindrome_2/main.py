def is_palindrome(s):

    left = 0
    right = len(s) - 1
    mismatch = 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if mismatch == 2:
                return False

            if mismatch == 0:
                left += 1
                mismatch += 1
            else:
                left -= 1
                right -= 1
                mismatch += 1

    return True


def main():
    strings = ["madame", "dead", "abca", "tebbem", "eeccccbebaeeabebccceea"]

    for i in range(len(strings)):
        print(i + 1, ".\t Actual string:\t\t" + strings[i], sep="")
        print("\t Is palindrome:\t\t", sep="", end="")
        print("True" if is_palindrome(strings[i]) else "False", sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
