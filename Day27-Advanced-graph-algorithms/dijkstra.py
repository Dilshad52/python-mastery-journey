import heapq

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 5)],
    "C": [("D", 1)],
    "D": []
}

def dijkstra(graph, start):
    distance = {node: float("inf") for node in graph}
    distance[start] = 0

    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = dist + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distance

result = dijkstra(graph, "A")

print("Shortest Distances:")

for node, dist in result.items():
    print(node, ":", dist)
