"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Ex 1:
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

[-3, 2, -3, 4, 2]
[-3, -1, -4, 0, 2]


Ex 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.


Ex 3:
Input: nums = [1,-2,-3]
Output: 5
"""
import math


def min_value(nums):
    ans = nums[0]
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
        ans = min(ans, nums[i])
    if ans < 1:
        return 1 - ans
    return 1


def min_value1(nums):
    ans = 0
    curr = 0
    for num in nums:
        curr += num
        ans = min(ans, curr)
    return 1 - ans


print(min_value([1, -2, -3]))
print(min_value([-3, 2, -3, 4, 2]))
print(min_value([1, 2]))
print(min_value([3, 2, 1]))
print(min_value([2, 3, 5, -5, -1]))
print(min_value([-12]))
print(min_value([-12, 15, 10]))
print(min_value([-2, -15, 10]))

print(min_value1([1, -2, -3]))
print(min_value1([-3, 2, -3, 4, 2]))
print(min_value1([1, 2]))
print(min_value1([3, 2, 1]))
print(min_value1([2, 3, 5, -5, -1]))
print(min_value1([-12]))
print(min_value1([-12, 15, 10]))
print(min_value1([-2, -15, 10]))
