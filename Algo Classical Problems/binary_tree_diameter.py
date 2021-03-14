"""
Given a binary tree, find its diameter - largest number of nodes connected in a path

TODO: Iterative version
"""

def get_binary_tree_diameter_and_height(tree):
    """
    Given a binary tree, returns the longest path of connected nodes & height

    O(n) time
    O(n) space for recursion
    """

    # leaf node has 0 diameter & height (base case)
    if not tree:
        return 0, 0

    # calculate the left and right sub tree diameter & height
    left_diameter, left_height = get_binary_tree_diameter_and_height(tree.left)
    right_diameter, right_height = get_binary_tree_diameter_and_height(tree.right)

    # figure out which diameter is longer
    path_through_node = left_height + right_height
    max_sub_tree_diameter = max(left_diameter, right_diameter)
    node_diameter = max(path_through_node, max_sub_tree_diameter)
    
    # calculate the height of the curr node
    node_height = max(left_height, right_height) + 1

    return node_diameter, node_height

if __name__ == "__main__":
    unittest.main()
    

    
