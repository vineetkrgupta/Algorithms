"""
Notes:
    - Can be used to solve maze problems.
    - Always gives optimal solution if one exists.
    - Requires a lot of memory for dense maps/layouts.
    - Uses Breadth first search algorithm and queues.

Applications:
    - Maze solving.
    - Routing.

References:
    - https://hyperskill.org/learn/step/6406
"""
import unittest

def lee_algorithm():
    """Solves the maze and returns the path from start to end"""

    # 1. Choose a starting point and add it to the queue
    # 2. Add valid neighbors to the queue (Check and see if neighbors are blocked)
    # 3. Remove position from queue and continue to next position
    # 4. Repeat until the queue is empty.
    # 5. If end position is reached then you solved the maze.

class TestLeeAlgorithm(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
