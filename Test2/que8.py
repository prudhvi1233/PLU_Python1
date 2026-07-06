'''
8.Check whether a stack is empty and display an appropriate message
'''

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack is not empty")

s = Stack()

s.is_empty()