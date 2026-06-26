class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top:", stack.peek())
print("Popped:", stack.pop())
print("Stack:", stack.items)
