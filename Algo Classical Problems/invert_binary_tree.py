"""Algorithm to invert a binary tree"""
import unittest
import queue

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree_recursive(tree):
    """Recursive implementation of the binary tree inversion algorithm"""

    if not tree:
        return

    invert_binary_tree_recursive(tree.left)
    invert_binary_tree_recursive(tree.right)

    tree.left, tree.right = tree.right, tree.left
    return tree

def invert_binary_tree_iterative(tree):
    """Iterative implementation of the binary tree inversion algorithm"""

    if not tree:
        return

    to_visit = queue.Queue()
    to_visit.put(tree)

    while not to_visit.empty():
        node = to_visit.get()

        if not node:
            continue
        
        # invert the left and right sub trees
        node.left, node.right = node.right, node.left
        
        # add nodes to be processed
        to_visit.put(node.left)
        to_visit.put(node.right)

    return tree

if __name__ == "__main__":
    unittest.main()
