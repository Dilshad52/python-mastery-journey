from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.items:
            return self.items.popleft()

    def front(self):
        if self.items:
            return self.items[0]


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front:", queue.front())
print("Dequeued:", queue.dequeue())
print("Queue:", list(queue.items))
