"""
Breadth first search is an algorithm that is useful to find a shortest path given a tree or graph.
BFS uses a queue in its implementation.

Notes:
    1. May use more memory than a DFS search since number of nodes in a level is usually more than
    the height.
    2. Complexity of DFS & BFS is O(N + M) - nodes & edges
"""
import queue
import unittest

class TreeNode(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first_search(root, target):
    """Check if target exists within the tree"""

    if not root:
        return False

    # BFS algorithm uses a queue to track the nodes to visit next
    to_visit = queue.Queue()
    to_visit.put(root)

    # Visited set is used to skip processed nodes already - useful in graph
    visited = set([root])

    while not to_visit.empty():
        curr_node = to_visit.get()

        if curr_node._value == target:
            return True

        # for a graph, use appropriate method to get the 
        # array of neighbors for the curr_node
        for child in [curr_node.left, curr_node.right]:
            if child is curr_node:
                raise Exception("Loop detected")
            
            if child and child not in visited:
                to_visit.put(child)
                
        visited.add(curr_node)

    return False
    
class TestBreadthFirstSearch(unittest.TestCase):

    def test_empty_node(self):
        self.assertEqual(breadth_first_search(None, 15), False)

    def test_single_node_tree(self):
        pass

    def test_two_node_tree(self):
        pass

    def test_tree_with_loop(self):
        pass

    def test_tree_with_cycle(self):
        pass

    def test_tree_with_target(self):
        pass

    def test_tree_without_target(self):
        pass

if __name__ == "__main__":
    unittest.main()
