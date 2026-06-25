class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    current.next = l1 or l2

    return dummy.next


def display(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

result = merge(l1, l2)

display(result)
