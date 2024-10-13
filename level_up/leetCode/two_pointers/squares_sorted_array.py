"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

ex: 1
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

ex: 2
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""


def squares_sorted(arr):
    n = len(arr)
    if n == 0:
        return arr

    left = 0
    right = n - 1
    res = [0] * n
    n -= 1

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            res[n] = arr[left] * arr[left]
            left += 1
            n -= 1
        else:
            res[n] = arr[right] * arr[right]
            right -= 1
            n -= 1

    return res


print(squares_sorted([-4, -1, 0, 3, 10]))

print(squares_sorted([]))

print(squares_sorted([1, 2, 2, 3]))

print(squares_sorted([-5, -3, -2, -2, 0]))

print(squares_sorted([0]))

print(squares_sorted([0, 1, 2]))
