'''
5.Create an empty stack and push the values 5, 10, 15, 20 into it. Display
the stack.
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def display(self):
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])

s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

s.display()
