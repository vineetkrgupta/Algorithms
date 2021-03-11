"""
Depth first search is one of the fundamental search algorithms for graphs or trees.

Pros:
    1. It uses less memory than BFS 

Cons:
    1. Is usually slower than BFS to find the shortest path
"""

def depth_first_search(root, target):
    """Performs the depth first search algorithm and returns node or None"""

    nodes_to_visit = [root]

    # You can add the root here to skip checking for loops
    visited = Set()

    while nodes_to_visit:
        curr_node = nodes_to_visit.pop()

        if curr_node.value == target:
            return curr_node

        for next_node in [curr_node.left, curr_node.right]:
            
            if next_node is curr_node:
                raise Exception("Loop detected")
           
            # avoid cycles
            if next_node and next_node not in visited:
                nodes_to_visit.add(next_node)

        visited.add(curr_node)

    return None
