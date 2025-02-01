"""
A tree is a hierarchical data structure consisting of nodes, where each node has a value and may have child nodes.
 The top node is called the root, and nodes without children are called leaves.

A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def print_tree(self, node):
        if node is not None:
            self.print_tree(node.left)
            print(node.value)
            self.print_tree(node.right)

# Example usage
bt = BinaryTree(1)
bt.insert_left(bt.root, 2)
bt.insert_right(bt.root, 3)
bt.insert_left(bt.root.left, 4)
bt.print_tree(bt.root)  # Output: 4 2 1 3

