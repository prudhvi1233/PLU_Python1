'''
16.Find and display all the leaf nodes of a binary tree.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

def leaf_nodes(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        print(node.data, end=" ")

    leaf_nodes(node.left)
    leaf_nodes(node.right)

leaf_nodes(root)