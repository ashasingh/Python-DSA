# To install the module; pip install binarytree
#
from binarytree import Node
root = Node(3)
root.left = Node(6)
root.right = Node(8)

# Getting binary tree
print('Binary tree :', root)

# Getting list of nodes
print('List of nodes :', list(root))

# Getting inorder of nodes
print('Inorder of nodes :', root.inorder)

# Checking tree properties
print('Size of tree :', root.size)
print('Height of tree :', root.height)

# Get all properties at once
print('Properties of tree : \n', root.properties)


# Creating binary tree
# from given list
from binarytree import build

# List of nodes
nodes =[3, 6, 8, 2, 11, None, 13]

# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
	binary_tree)

# Getting list of nodes from
# binarytree
print('\nList from binary tree :',
	binary_tree.values)

#Build a random binary tree:
#tree() generates a random binary tree and returns its root node.

from binarytree import tree

# Create a random binary
# tree of any height
root = tree()
print("Binary tree of any height :")
print(root)

# Create a random binary
# tree of given height
root2 = tree(height = 2)
print("Binary tree of given height :")
print(root2)

# Create a random perfect
# binary tree of given height
root3 = tree(height = 2,
			is_perfect = True)
print("Perfect binary tree of given height :")
print(root3)


## this module is further used to create heaps and bst
