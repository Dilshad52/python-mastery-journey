import heapq

tasks = []

heapq.heappush(tasks, (2, "Email"))
heapq.heappush(tasks, (1, "Fix Server"))
heapq.heappush(tasks, (3, "Meeting"))
heapq.heappush(tasks, (1, "Database Backup"))

print("Priority Queue:")

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, task)
