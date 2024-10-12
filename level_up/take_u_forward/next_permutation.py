def nextPermutation(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    global temp, j

    for i in range(len(nums) - 1, -1, -1):
        # print("1st" + str(i))
        if nums[i] > nums[i - 1] and (i - 1) > -1:
            print("i : " + str(i))
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    print("nums[j]" + str(nums[j]))
                    temp = nums[i-1]
                    break
            print("j : " + str(nums[j]))
            nums[i-1] = nums[j]
            nums[j] = temp
            print(nums)
            print(nums[i:len(nums)-1:-1])
            nums = nums[:j] + nums[j::-1]
            break

    # print("2nd" + str(i))
    if i <= 0:
        nums.reverse()



# nums = [1, 1, 5]
nums = [1, 3, 2]
# nums = [3, 2, 1]
print(nums)
nextPermutation(nums)
print(nums)