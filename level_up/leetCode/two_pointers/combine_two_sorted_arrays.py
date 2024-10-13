"""
Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
"""


def combine_sorted_arrays(arr1, arr2):
    left1 = left2 = 0
    n1 = len(arr1)
    n2 = len(arr2)
    result = []

    while left1 < n1 and left2 < n2:
        if arr1[left1] <= arr2[left2]:
            result.append(arr1[left1])
            left1 += 1
        else:
            result.append(arr2[left2])
            left2 += 1

    while left1 < n1:
        result.append(arr1[left1])
        left1 += 1

    while left2 < n2:
        result.append(arr2[left2])
        left2 += 1

    return result


print(combine_sorted_arrays([1, 2, 3], [4, 5, 6]))

print(combine_sorted_arrays([1, 4, 6], [2, 3, 5]))

print(combine_sorted_arrays([1], [4, 5, 6]))

print(combine_sorted_arrays([1], []))

print(combine_sorted_arrays([], [1]))

print(combine_sorted_arrays([], []))

print(combine_sorted_arrays([1, 2], [1]))

print(combine_sorted_arrays([2], [1]))
