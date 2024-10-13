"""
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
return a boolean array that represents the answer to each query.

A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13,
the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
"""

# nums   = [1, 6, 3, 2, 7, 2]
# prefix = [1, 7, 10, 12, 19, 21]
#
# [0, 3] => 12 (12 - 1 + 1)
# [2, 5] => 14 (21 - 10 + 3)
# [2, 4] => 12 (19 - 10 + 3)
#
# queries = [[0, 3], [2, 5], [2, 4]]
# limit = 13


def answer_queries(nums, queries, limit):

    prefix_sum = [nums[0]]
    ans = []
    
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[i-1] + nums[i])

    for i in range(len(queries)):
        (start, end) = queries[i]
        curr = prefix_sum[end] - prefix_sum[start] + nums[start]
        ans.append(curr < limit)

    return ans


print(answer_queries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))
