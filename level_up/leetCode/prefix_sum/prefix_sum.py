def prefix_sum(nums):
    ans = [nums[0]]
    for i in range(1, len(nums)):
        ans.append(ans[i-1] + nums[i])
    return ans


def prefix_sum1(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


print(prefix_sum([1, 2, 3, 4]))
print(prefix_sum1([1, 2, 3, 4]))
