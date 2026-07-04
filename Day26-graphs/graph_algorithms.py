def connected_components(graph):
    visited = set()

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count


def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False


graph1 = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}

graph2 = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

print("Connected Components:", connected_components(graph1))
print("Cycle Present:", has_cycle(graph2))
