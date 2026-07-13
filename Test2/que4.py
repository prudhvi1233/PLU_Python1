'''
4.Count and display the total number of nodes in the linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

temp = head
count = 0

while temp:
    count += 1
    temp = temp.next

print("Total number of nodes:", count)