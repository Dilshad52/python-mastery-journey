from functools import reduce

nums = [1,2,3,4,5,6]

even = filter(lambda x:x%2==0, nums)

squares = map(lambda x:x*x, even)

result = reduce(lambda x,y:x+y, squares)

print(result)
