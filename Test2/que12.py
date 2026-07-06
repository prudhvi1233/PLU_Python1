# 12.Display all the elements of the queue in FIFO order.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements in FIFO order:")
            for i in self.queue:
                print(i, end=" ")

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()
