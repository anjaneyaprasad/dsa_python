"""
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
"""


def largest_sum(nums, k):
    n = len(nums)
    if 0 == n or 0 == k:
        return 0

    if k > n:
        k = n

    curr = 0

    for i in range(k):
        curr += nums[i]

    ans = curr

    for i in range(k, n):
        curr += nums[i] - nums[i - k]
        ans = max(curr, ans)

    return ans


print(largest_sum([1, 2, 3, 4], 2))
print(largest_sum([1, 2, 3, 4], 3))
print(largest_sum([1, 2, 3, 4], 4))
print(largest_sum([1, 2, 3, 4], 5))
print(largest_sum([1, 2, 3, 4], 1))

