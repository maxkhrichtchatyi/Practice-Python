#!/bin/python3
# -*- coding: utf-8 -*-

"""
Write a function named firstNonRepeatingLetter† that takes a string input, and returns the first character that is not
repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the
string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return
the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return the empty string ("").

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any
Unicode character.
"""


def first_non_repeating_letter(string):
    letter = ''

    for char in string:
        if string.lower().count(char.lower()) == 1:
            letter = char
            break

    return letter


print('Run the "first_non_repeating_letter" function', end='\n')
print(first_non_repeating_letter('sTreSS'))
