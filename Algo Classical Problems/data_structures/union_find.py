"""
Notes:
Implementation of the union find datastructure.
- Keep track of a set of disjoint elements into a number of disjoint and nonoverlapping subsets.
- A find operation determines which subset a particular element is in.
- An union joins two subsets into a single one.
- Union by rank (Smaller tree to larger tree)
- Union by path compression (Flattening the structure of the tree)

The Approaches:
    - Quick Find (Eager approach).
    - Quick Union (Lazy approach).
    - Quick Union (Weighted).
    - Quick Union with path compression.

Applications:
    - Games.
    - Percolation.
    - Least Common Ancestor.
    - Dynamic Connectivity.
    - Kruskal's minimum spanning tree.
    - Image processing.
"""

