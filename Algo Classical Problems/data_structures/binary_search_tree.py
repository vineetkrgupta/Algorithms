"""
Notes:
    - A binary search tree is a binary tree with a special property
    - Every node has from 0 to 2 child nodes
    - BST property is the following
        - There are different variations of the property. 
            - Left <= Root <= Right (or)
            - Left < Root < Right (or)
            - Left < Root <= Right (or)
            - Left <= Root < Right
    - ADT
        - __contains__
        - closest_value
        - insert
        - remove
        - _balance
    - Trees can be imbalanced leading to performance issues.

Applications:
    - Variations of BST are AVL, Red Black trees are widely used in practice.
    - Databases
    - Priority Queue

References:
    - https://en.wikipedia.org/wiki/Binary_search_tree

TO-DO:
    - Add more documentation and information
"""
import unittest


class Node:
    """Node within a binary tree"""

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None


class BinarySearchTree(object):

    def __init__(self, value):
        self._root = Node(value)

    def _get_closest_node(self, value):
        """Travels to the closest node in the tree, if value is equal it returns the node"""
        parent_node = None
        curr_node = self._root
        while curr_node:
            parent_node = curr_node
            if value < curr_node._value:
                curr_node = curr_node._left
            elif value > curr_node._value:
                curr_node = curr_node._right
            else:
                break

        return parent_node

    def __contains__(self, value):
        """Test to see if the BST contains a given value"""
        closest_node = self._get_closest_node(value)
        return closest_node._value == value

    def insert(self, value):
        """Insert the given value into the BST"""
        closest_node = self._get_closest_node(value)
        # two cases
        # case I - insert in the middle of the tree (ex: root, parent)
        # case II - insert at leaf node
        if value < closest_node._value:
            left_node = closest_node._left
            closest_node._left = Node(value)
            closest_node._left._left = left_node
        else:
            right_node = closest_node._right
            closest_node._right = Node(value)
            closest_node._right._right = right_node

    def remove(self, value, parent_node=None):
        """Remove a given value from the tree, removes the first encountered value for repeated values"""

        # traverse to the node
        curr_node = self._root
        while curr_node:
            if value < curr_node._value:
                parent_node = curr_node
                curr_node = curr_node._left
            elif value > curr_node._value:
                parent_node = curr_node
                curr_node = curr_node._right
            else:
                break

        # case I - node has both children
        if curr_node._left and curr_node._right:
            # get the minimum value from the right sub tree and replace it with current value
            curr_node.value = curr_node._get_min_value(curr_node._right)
            # remove the node with min value

        # case II - deleting the root node
        elif not parent_node:
            # try to replace with left first
            # replace with right if left not available
            # both are not available? - its an edge case
            pass

        # case III - deleting nodes with only one left child
        elif parent_node._left == curr_node:
            pass

        # case IV - deleting nodes with only one right child
        elif parent_node._right == curr_node:
            pass

    def get_min_value(self, start_node=None):

        curr_node = start_node if start_node else self._root

        if not curr_node._left:
            return curr_node._value
        else:
            return self._get_min_value(curr_node._left)

    def in_order_traversal(self, node=None):
        """Returns a list with nodes traversed in-order: left, root, right"""

        if not node:
            node = self._root

        if node._left:
            self.in_order_traversal(node._left)
        print(node._value)
        if node._right:
            self.in_order_traversal(node._right)

    def pre_order_traversal(self, node=None):
        """Returns a list with nodes traversed pre-order: root, left, right"""

        if not node:
            node = self._root

        print(node._value)
        if node._left:
            self.pre_order_traversal(node._left)
        if node._right:
            self.pre_order_traversal(node._right)

    def post_order_traversal(self, node=None):
        """Returns a list with nodes traversed post-order: left, right, root"""

        if not node:
            node = self._root

        if node._left:
            self.post_order_traversal(node._left)
        if node._right:
            self.post_order_traversal(node._right)
        print(node._value)


class TestBinarySearchTree:

    def setUp(self):
        tree = TreeNode(5)
        tree.insert(1)
        tree.insert(10)
        tree.insert(3)
        tree.insert(2)
        tree.insert(7)
        tree.insert(8)
        tree.insert(4)
        tree.insert(9)
        tree.insert(6)
        self.tree = tree


def test_tree_traversal():
    """Test the tree implementation for simple cases"""


if __name__ == '__main__':
    unittest.main()
