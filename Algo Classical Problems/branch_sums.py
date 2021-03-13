"""
Given a binary tree, find all the sums of branches
"""
import unittest


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(root):

    stack = [root]
    path = []

    while len(path) <= 2:
        curr_node = stack.pop()

        if curr_node.left:
            stack.append(curr_node.left)
            continue

        if curr_node.right:
            stack.append(curr_node.right)

    print([node.value for node in path])
    return ([node.value for node in path])


def branch_sums(root):
    """Find the branch sums in a Binary tree"""

    traversal = [root]
    path = []
    sums = []
    while traversal:

        curr_node = traversal.pop()

        # remove all nodes that are disconnected
        while path and path[-1].left != curr_node and path[-1].right != curr_node:
            path.pop()

        path.append(curr_node)

        if curr_node.right:
            traversal.append(curr_node.right)

        if curr_node.left:
            traversal.append(curr_node.left)

        if not curr_node.left and not curr_node.right:
            sums.append(sum([node.value for node in path]))
            path.pop()

    return sums


class TestBranchSums(unittest.TestCase):

    def setUp(self):
        root = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)

        root.left = two
        root.right = three

        two.left = four
        two.right = five
        self.binary_tree = root

    def test_sample(self):
        sums = branch_sums(self.binary_tree)
        self.assertEqual(sums, [7, 8, 4])


if __name__ == "__main__":
    unittest.main()
