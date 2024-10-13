"""Given a sorted array of unique integers and a target integer,
    return true if there exists a pair of numbers that sum to target,
    false otherwise.
"""


def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return True
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1

    return False


print(check_for_target([1, 2, 4, 6, 8, 9, 14, 15], 13))

print(check_for_target([1, 2, 4], 6))

print(check_for_target([1, 2], 13))

print(check_for_target([1], 13))

print(check_for_target([], 13))
