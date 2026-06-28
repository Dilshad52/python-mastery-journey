class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, target):
    if root is None:
        return False

    if root.data == target:
        return True

    if target < root.data:
        return search(root.left, target)

    return search(root.right, target)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print(search(root, 7))
print(search(root, 100))
