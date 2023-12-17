def replace_multiple_spaces_with_single_space(string):
    result = []
    space = False

    for char in string:
        if char.isspace():
            if not space:
                result.append(char)
                space = True
        else:
            result.append(char)
            space = False

    return "".join(result)


def rev_str(string, start=None, end=None):
    start = start if start else 0
    end = end if end else len(string) - 1

    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

    return string


def reverse_words(sentence):
    sentence = replace_multiple_spaces_with_single_space(sentence.strip())
    sentence = list(sentence)
    sentence = rev_str(sentence)

    # set pointers
    start = 0
    end = 0
    sentence_length = len(sentence)

    while start < sentence_length:
        while end < sentence_length and sentence[end] != " ":
            end += 1

        rev_str(sentence, start, end - 1)
        start = end + 1
        end += 1

    return "".join(sentence)


def main():
    string_to_reverse = [
        "Hello Friend",
        "    We love Python",
        "The quick brown fox jumped over the lazy dog   ",
        "Hey",
        "To be or not to be",
        "AAAAA",
        "Hello     World",
    ]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\t Actual string:\t\t" + "".join(string_to_reverse[i]), sep="")
        Result = reverse_words(string_to_reverse[i])
        print("\t Reversed string:\t" + "".join(Result), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
