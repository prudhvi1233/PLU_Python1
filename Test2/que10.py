'''
10. Remove one element from the front of the queue and display the updated
queue.
'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            self.queue.pop(0)

    def display(self):
        for i in self.queue:
            print(i, end=" ")

q = Queue()

q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)

q.dequeue()

q.display()