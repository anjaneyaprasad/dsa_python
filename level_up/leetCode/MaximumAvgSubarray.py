
def find_max_avg(nums, k):
    running_sum = 0
    n = len(nums)

    for i in range(0, k):
        running_sum += nums[i]
    res = running_sum
    for i in range(k, n):
        running_sum += nums[i] - nums[i-k]
        res = max(res, running_sum)

    return res/k


# input_array = [1, 12, -5, -6, 50, 3]
input_array = [0, 1, 1, 3, 3]
window_size = 4
print(find_max_avg(input_array, window_size))
