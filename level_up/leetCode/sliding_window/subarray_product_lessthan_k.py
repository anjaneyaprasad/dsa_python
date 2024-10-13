"""
Given an array of positive integers nums and an integer k, return the number of subarrays where
the product of all the elements in the subarray is strictly less than k.

For example,
given the input nums = [10, 5, 2, 6], k = 100, the answer is 8.

The subarrays with products less than k are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""


def product_k(nums, k):
    if k <= 1:
        return 0
    n = len(nums)
    if n == 0:
        return 0

    left = ans = 0
    curr = 1

    for right in range(n):
    # for right, num in enumerate(nums):
        curr *= nums[right]
        # curr *= num
        while curr >= k:
            curr /= nums[left]
            left += 1
        ans += (right - left + 1)

    return ans


print(product_k([10, 5, 2, 6], 100))
print(product_k([10, 5, 2, 6], 20))  # [10], [5], [2], [5, 2], [6], [2, 6]
print(product_k([], 100))
print(product_k([10, 5, 2, 6], 1000))
print(product_k([10, 5, 2, 6], 5))
print(product_k([10, 5, 2, 6], 0))
print(product_k([1, 1, 1], 1))
print(product_k([2, 2, 2], 2))
print(product_k([57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], 18))
