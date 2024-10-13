"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters
from the original string, while maintaining the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde" while "aec" is not.
"""


def subsequence(input_string, subsequence):
    left1 = left2 = 0
    n1 = len(input_string)
    n2 = len(subsequence)

    if 0 == n2:
        return False

    while left1 < n1 and left2 < n2:
        if input_string[left1] == subsequence[left2]:
            left2 += 1
        left1 += 1

    if left2 == n2:
        return True

    return False


print(subsequence("abcde", "ace"))
print(subsequence("abcde", "acf"))
print(subsequence("Anjaneya", "Ajy"))
print(subsequence("Anjaneya", "Anji"))
print(subsequence("", "ace"))
print(subsequence("abcde", ""))
print(subsequence("ace", "abcde"))
