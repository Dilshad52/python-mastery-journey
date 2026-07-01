import heapq

numbers = [30, 10, 50, 20]

heapq.heapify(numbers)

print("Min Heap:", numbers)

heapq.heappush(numbers, 5)

print("After Insert:", numbers)

smallest = heapq.heappop(numbers)

print("Removed Smallest:", smallest)

print("Heap After Removal:", numbers)

print("Minimum Element:", numbers[0])

max_heap = []

for num in [10, 20, 30]:
    heapq.heappush(max_heap, -num)

print("Largest Element:", -heapq.heappop(max_heap))
