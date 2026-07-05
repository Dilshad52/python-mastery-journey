parent = {}

def make_set(x):
    parent[x] = x

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x

for i in range(1, 6):
    make_set(i)

union(1, 2)
union(2, 3)
union(4, 5)

print("Parent Dictionary:")
print(parent)

print()

print("Find(3):", find(3))
print("Find(5):", find(5))

print()

print("1 and 3 Connected:", find(1) == find(3))
print("2 and 5 Connected:", find(2) == find(5))
