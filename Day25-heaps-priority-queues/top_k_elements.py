import heapq

numbers = [15, 4, 8, 25, 16, 42, 9, 30]

print("Three Largest:")
print(heapq.nlargest(3, numbers))

print()

print("Two Smallest:")
print(heapq.nsmallest(2, numbers))

print()

list1 = [1, 4, 7]
list2 = [2, 5, 8]

merged = list(heapq.merge(list1, list2))

print("Merged Sorted Lists:")
print(merged)
