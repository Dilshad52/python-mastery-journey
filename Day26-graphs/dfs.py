graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        dfs(neighbor)

print("DFS Traversal:")
dfs("A")
