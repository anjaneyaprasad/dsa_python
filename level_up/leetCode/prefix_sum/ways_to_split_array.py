"""
Given an integer array nums, find the number of ways to split the array into two parts so that
the first section has a sum greater than or equal to the sum of the second section.
The second section should have at least one number.

ex 1:
[10, 4, -8, 7]

[10], [4, -8, 7]  √
[10, 4], [-8, 7]  √
[10, 4, -8], [7]  x
[10, 4, -8, 7],[] x

possible ways: 2

[10, 4, -8, 7]
prefix:
[10, 14, 6, 13]

[10], [3] ==> 13-14+4
[14], [-1] ==> 13-6-8
[6], [7] ==> 13-13+7


left: [10, 14, 6, 13]
right: [13, 3, -1, 7]
"""
from typing import List


def ways_to_split(nums):
    n = len(nums)
    prefix_sum = [0]*n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = nums[i] + prefix_sum[i - 1]
    ans = 0
    for i in range(n - 1):
        if prefix_sum[i] >= prefix_sum[-1] - prefix_sum[i + 1] + nums[i + 1]:
            ans += 1
    return ans


def ways_to_split2(nums):
    n = len(nums)
    left = [0] * n
    right = [0] * n
    left[0] = nums[0]
    for i in range(1, n):
        left[i] = left[i-1] + nums[i]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] + nums[i+1]
    ans = 0
    for i in range(n-1):
        if left[i] >= right[i]:
            ans += 1
    return ans


def ways_to_split3(nums):
    total = sum(nums)
    left = 0
    ans = 0
    for i in range(len(nums) - 1):
        left += nums[i]
        right = total - left
        if left >= right:
            ans += 1
    return ans


def waysToSplitArray(nums: List[int]) -> int:
    lsum, rsum, ans = 0, sum(nums), 0
    for i in range(len(nums) - 1):
        lsum += nums[i]
        rsum -= nums[i]
        ans += (lsum >= rsum)
    return ans


print(ways_to_split([10, 4, -8, 7]))
print(ways_to_split2([10, 4, -8, 7]))
print(ways_to_split3([10, 4, -8, 7]))
print(waysToSplitArray([10, 4, -8, 7]))
