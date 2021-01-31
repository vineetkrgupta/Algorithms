"""
Weighted graph is an important data structure. Especially useful to find shortest path using
dijkstra's algorithm in a constricted environment represented by their weights.

Applications:
    - Computer Networks
    - Social Networks
    - Geospatial mapping & routing

Representations:
    - Edge List
    - Adjacency list
    - Adjacency matrix

ADT:
    - add_vertex(vertex)
    - add_edge(vertex1, vertex2)
"""
class WeightedGraph(object):
    """Weighted graphs use weights to represent contriction on edges"""

    class Vertex(object):
        """Represents a vertex in a graph""" 

        def __init__(self, value):
            self._value = value
            
            # Adjacency list
            self._edges = []

        @property
        def value():
            return self._value

       
