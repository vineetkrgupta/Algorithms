"""
Traversing a given binary tree the following ways
1. In-order traversal
2. Pre-order traversal
3. Post-order traversal
"""

class BinaryTree(object):
    """Object that represents a binary tree node"""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(tree, path=[]):
    """Visit left -> curr -> right"""

    if tree:
        in_order_traversal(tree.left, path)
        path.append(tree.value, path)
        in_order_traversal(tree.right, path)

    return path
        
def pre_order_traversal(tree, path=[]):
    """Visit curr -> left -> right"""

    if tree:
        path.append(tree.value)
        pre_order_traversal(tree.left, path)
        pre_order_traversal(tree.right, path)

    return path

def post_order_traversal(tree, path=[]):
    """Visit left, right, curr"""

    if tree:
        post_order_traversal(tree.left, path)
        post_order_traversal(tree.right, path)
        path.append(tree.value)

    return path
    
