'''
14.Perform an Inorder Traversal on a binary tree.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Create the binary tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)

print("Inorder Traversal:")
inorder_traversal(root)