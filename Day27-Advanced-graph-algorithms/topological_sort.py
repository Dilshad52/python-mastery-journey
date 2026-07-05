from collections import deque

graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": [],
    "D": []
}

indegree = {node: 0 for node in graph}

for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

queue = deque()

for node in indegree:
    if indegree[node] == 0:
        queue.append(node)

print("Topological Order:")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)
