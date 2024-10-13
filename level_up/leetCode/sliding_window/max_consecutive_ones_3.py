"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can
flip at most k 0's.

Ex 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]

Ex 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
"""


def max_consecutive_ones(nums, k):
    n = len(nums)

    if 0 == n or 0 == k:
        return 0

    if k > n:
        k = n

    curr = ans = left = 0

    for right in range(n):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


print(max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))


# def longestOnes(self, nums: List[int], k: int) -> int:
#     left = 0
#     for right in range(len(nums)):
#         # If we included a zero in the window we reduce the value of k.
#         # Since k is the maximum zeros allowed in a window.
#         if nums[right] == 0:
#             k -= 1
#         # A negative k denotes we have consumed all allowed flips and window has
#         # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
#         if k < 0:
#             # If the left element to be thrown out is zero we increase k.
#             if nums[left] == 0:
#                 k += 1
#             left += 1
#     return right - left + 1


# object Solution {
#     def longestOnes(nums: Array[Int], k: Int): Int = {
#         var l = 0
#         var r = 0
#         var maxLen = 0
#         var len = 0
#         while(r <= nums.length) {
#             len = nums.slice(l, r).count(_ == 0)
#             len match {
#                 case _ if len < k =>
#                 if(r != nums.length) {
#                     r += 1
#                 } else {
#                     maxLen = Math.max(maxLen, nums.slice(l, r).length)
#                     r += 1
#                 }
#                 case _ if len == k =>
#                 maxLen = Math.max(maxLen, nums.slice(l, r).length)
#                 r += 1
#                 case _ if len > k =>
#                 l += 1
#             }
#         }
#         maxLen
#     }
# }
