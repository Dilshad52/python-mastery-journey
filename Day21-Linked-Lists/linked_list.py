class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_beginning(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_end(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def search(self, target):

        current = self.head

        while current:

            if current.data == target:
                return True

            current = current.next

        return False

    def delete(self, key):

        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next


ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)

print("Linked List:")
ll.display()

print("Search 20:", ll.search(20))

ll.delete(20)

print("After Deleting 20:")
ll.display()
