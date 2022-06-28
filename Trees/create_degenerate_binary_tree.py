# Checking if a binary tree is a Degenerate or Pathological Tree in Python

# Creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

# Checking Degenerate or Pathological Tree
def isDenTree(root):
    # Tree empty case
    if root is None:
        return True

    # Checking whether both child are present
    if root.leftChild is not None and root.rightChild is not None:
        return False

    # if either one child present
    if root.leftChild is None or root.rightChild is None:
        return (isDenTree(root.leftChild) and isDenTree(root.rightChild))

    return False

# create a tree
root = Node(1)
root.rightChild = Node(3)
root.rightChild.leftChild = Node(4)

# check if its degenerate or not
if isDenTree(root):
    print("The tree is a Degenerate or Pathological binary tree")
else:
    print("The tree is not a Degenerate or Pathological binary tree")
    
# add another node to make it non-degenerate
root.leftChild = Node(2)
if isDenTree(root):
    print("The tree is a Degenerate or Pathological binary tree")
else:
    print("The tree is not a Degenerate or Pathological binary tree")
