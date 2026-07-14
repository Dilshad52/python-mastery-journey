# ---------------------------------------
# Day 29 - Coding Interview Patterns
# ---------------------------------------

# 1. Two Pointers

print("Two Pointers Result:")

nums = [1, 2, 3, 4, 7, 8]
left = 0
right = len(nums) - 1
target = 11

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        print(nums[left], nums[right])
        break
    elif total < target:
        left += 1
    else:
        right -= 1

print()
--------------------------------------------------------------------------------------------

# 2. Sliding Window

print("Maximum Sliding Window Sum:")

nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k])
maximum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i-k]
    maximum = max(maximum, window_sum)

print(maximum)

print()
----------------------------------------------------------------------------------------------

# 3. Prefix Sum

print("Prefix Sum Array:")

nums = [2, 4, 6, 8]

prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)

print(prefix)

print()
----------------------------------------------------------------------------------------------

# 4. Hashing (Two Sum)

print("Two Sum Indices:")

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):
    diff = target - num

    if diff in seen:
        print(seen[diff], i)
        break

    seen[num] = i

print()
---------------------------------------------------------------------------------------------

# 5. Binary Search

print("Binary Search Index:")

nums = [1, 3, 5, 7, 9, 11]

target = 7

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print(mid)
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print()
-----------------------------------------------------------------------------------------------

# 6. Monotonic Stack

print("Next Greater Elements:")

nums = [2, 1, 5, 3]

stack = []
result = [-1] * len(nums)

for i in range(len(nums) - 1, -1, -1):

    while stack and stack[-1] <= nums[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(nums[i])

print(result)
