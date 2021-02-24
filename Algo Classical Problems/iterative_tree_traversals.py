"""
Iterative versions of the tree traversals

TODO: Using a set defeats the purpose of iteration (reducing the space usage)
"""

class BinaryTree(object):
    """Object represents a binary tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(tree):
    """left -> curr -> right"""

    to_visit = [tree]
    visited = set()
    path = []

    while to_visit:
        # peek to make sure it is not visited
        node = to_visit[-1]
        if node.left and node.left not in visited:
            to_visit.append(node.left)
            continue
            
        # we have to make sure we visit left before visiting current
        node = to_visite.pop()
        path.append(node.value)
        
        if node.right:
            to_visit.append(node.right)

    return path

def pre_order_traversal(tree):
    """curr -> left -> right"""

    to_visit = [tree]
    path = []
    
    while to_visit:
        node = to_visit.pop()
       
        path.append(node.value)

        # Stack is FIFO, append right first
        # TODO: there has to be a cleaner way to do it
        if node.right:
            to_visit.append(node.right)

        if node.left:
            to_visit.append(node.left)

    return path
        
def post_order_traversal(tree):
    """left -> right -> curr"""

    to_visit = [tree]
    visited = set()
    path = []

    while to_visit:

        node = to_visit[-1]

        # make sure we visit left before right
        if node.left and node.left not in visited:
            to_visit.append(node.left)
            continue

        # make sure we visit right before curr
        if node.right and node.right not in visited:
            to_visit.append(node.right)
            continue

        # since we visited both left and right, we can visit node
        to_visit.pop()
        path.append(node.value)

    return path
        
