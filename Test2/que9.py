'''
9.Create a queue and insert the values 10, 20, 30, 40.
'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def display(self):
        for i in self.queue:
            print(i)

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()
