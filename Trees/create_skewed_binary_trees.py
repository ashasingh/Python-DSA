# Checking if a binary tree is a left-skewed or right-skewed Tree in Python

# Creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

# Checking Degenerate or Pathological Tree
def isLeftSkewedTree(root):
    # Tree empty case
    if root is None:
        return True

    # Checking whether both child are present
    if root.leftChild is not None and root.rightChild is not None:
        return False
    
    # check if right is present
    if root.rightChild is not None:
        return False

    # if either one child present
    if root.leftChild is not None:
        return isLeftSkewedTree(root.leftChild)
    return True

def isRightSkewedTree(root):
    # Tree empty case
    if root is None:
        return True

    # Checking whether both child are present
    if root.leftChild is not None and root.rightChild is not None:
        return False
    
    # check if right is present
    if root.leftChild is not None:
        return False

    # if either one child present
    if root.rightChild is not None:
        return isRightSkewedTree(root.rightChild)
    return True

# create a tree
root = Node(1)
root.rightChild = Node(3)
root.rightChild.rightChild = Node(7)

# check if right skewed or not
if isLeftSkewedTree(root):
    print("The tree is a left skewed binary tree")
elif isRightSkewedTree(root):
    print("The tree is a right skewed binary tree")
else:
    print("The tree is not a skewed binary tree")

# modify and create left skewed
root.rightChild = None
root.leftChild = Node(3)

# check if left skewed or not
if isLeftSkewedTree(root):
    print("The tree is a left skewed binary tree")
elif isRightSkewedTree(root):
    print("The tree is a right skewed binary tree")
else:
    print("The tree is not a skewed binary tree")

root.leftChild.rightChild = Node(5)
root.leftChild.leftChild = Node(4)
# check if left skewed, right skewed or not
if isLeftSkewedTree(root):
    print("The tree is a left skewed binary tree")
elif isRightSkewedTree(root):
    print("The tree is a right skewed binary tree")
else:
    print("The tree is not a skewed binary tree")
