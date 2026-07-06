'''
15.Count the total number of nodes present in a binary tree.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    else:
        left_count = count_nodes(root.left)
        right_count = count_nodes(root.right)
        return left_count + right_count + 1

root = Node(50)
root.left = Node(30)
root.right = Node(70)

print("Total number of nodes:", count_nodes(root))