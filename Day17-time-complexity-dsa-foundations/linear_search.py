def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [10, 20, 30, 40]
print(linear_search(nums, 30))
