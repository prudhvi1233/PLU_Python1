# 11.Display the front element of the queue without removing it.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.front()
