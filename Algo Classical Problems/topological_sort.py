"""
Notes:
    - For directed acylic graphs only
    - Modification of DFS to do topological sort

Applications:
    - Job scheduling given dependencies
    - Spreadsheet's cell evauluation
    - Order of compilation tasks
    - Data serialization
    - Resolve symbol dependencies in linkers

References:
    - https://www.geeksforgeeks.org/topological-sorting/

TO-DO:
    - Recursive implementation is incomplete
    - Write non-recursive solution which performs better memory wise
"""

from collections import defaultdict

class Graph:
    
    def __init__(self, num_vertices):
        """Adjacency list representation"""
        self._graph = defaultdict(list)
        self._num_vertices = num_vertices

    def add_edge(self, vetex_u, vertex_v):
        """Add an edge from vertex u to vertex v"""
        self._graph[vertex_u].append(vertex_v)

    def recursive_topological_sort(self, vertex, visited, stack):
        """Recursive implementation"
        
        visited.add(vertex)
        
        for neighbor in self._graph[vertex]:
            if neighbor not in visited:
                self.recursive_topological_sort(neighbor, visited, stack)

        stack.append(vertex)

    def topological_sort(self):
        """
        Perform topological sorting on the graph
        Runtime - O(V + E)
        Space - O(V)
        """
        
        visited = Set()
        stack = []
            
        for vertex in range(self._num_vertices):
            if vertex not in visited:
                self.recursive_topological_sort(vertex, visited, stack)

        print(stack)

    


