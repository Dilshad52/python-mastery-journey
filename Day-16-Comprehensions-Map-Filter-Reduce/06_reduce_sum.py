from functools import reduce

nums = [10,20,30,40]

result = reduce(lambda x,y:x+y, nums)

print(result)
