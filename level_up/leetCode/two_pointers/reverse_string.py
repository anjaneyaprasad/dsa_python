"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


def reverse_string(input_string):
    left = 0
    right = len(input_string) - 1

    while left < right:
        tmp = input_string[left]
        input_string[left] = input_string[right]
        input_string[right] = tmp
        left += 1
        right -= 1

    return input_string


print(reverse_string(["A", "n", "j", "a", "n", "e", "y", "a"]))
print(reverse_string(["A", "B"]))
print(reverse_string([]))
