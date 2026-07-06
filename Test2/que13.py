'''
13.Create the following binary tree:
50
/ \
3070
Display the root, left child, and right child.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)

left_node = Node(30)
right_node = Node(70)

root.left = left_node
root.right = right_node

print("Root Node:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)

