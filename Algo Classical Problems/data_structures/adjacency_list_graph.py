"""Adjacency list is a graph representation using array or a hash map"""
from collections import deque


class AdjacencyListGraph:
    """Graph representation using dictionary"""

    def __init__(self):
        self.__nodes = {}

    def __str__(self):
        return str(self.__nodes)

    def insert_vertex(self, data):
        """Insert a vertex and its relationships """
        self.__nodes[data] = set()

    def insert_edge(self, start_data, end_data):
        """Insert a relationship b/w edges"""
        adj_list_start = self.__nodes.get(start_data, None)
        adj_list_end = self.__nodes.get(end_data, None)

        if adj_list_start is not None and adj_list_end is not None:
            adj_list_start.add(end_data)
            adj_list_end.add(start_data)
        else:
            raise Exception('vertexes are not found')

    def depth_first_search_path(self, source, destination, visited=None):
        """Looks for a path from source - destination"""
        print(source, visited)

        if visited is None:
            visited = set()

        # the source and destination must be vertices in the graph
        if source not in self.__nodes or destination not in self.__nodes:
            return False

        # if we looked through the source already
        # then the path does not exist
        if source in visited:
            return False

        # add to the visited list
        visited.add(source)

        # if the source and destination are equal then we found a path
        if source == destination:
            return True

        # ask the adj vertices to see if the path exists
        for adj_vertex in self.__nodes[source]:
            if self.depth_first_search_path(adj_vertex, destination, visited):
                return True

        # if the adj list is exhausted then return False as path does not exist
        return False

    def breadth_first_search(self, source, destination):
        """Do a breadth first search - queue & set"""

        visited = set()

        # source and destination must be valid vertices in the graph
        if source not in self.__nodes or destination not in self.__nodes:
            return False

        # create a queue and add source to it
        queue = deque()
        queue.appendleft(source)

        while len(queue):
            vertex = queue.pop()

            if vertex == destination:
                return True

            # if the vertex is already visited, nothing to do
            if vertex in visited:
                continue

            # add to visited set
            visited.add(vertex)

            # at the end add all of the adj vertices to the queue
            for adj_vertex in self.__nodes[vertex]:
                queue.appendleft(adj_vertex)

        return False


def create_graph():
    """Create and insert vertices and paths"""
    graph = AdjacencyListGraph()

    graph.insert_vertex(0)
    graph.insert_vertex(1)
    graph.insert_vertex(2)
    graph.insert_vertex(3)

    graph.insert_edge(0, 1)
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 3)

    return graph


def test_adjacency_list_graph():
    """Simple test for the graph implementation"""
    graph = create_graph()
    print(graph)


def test_dfs():
    """Depth first search a path"""
    graph = create_graph()
    print(graph.depth_first_search_path(0, 3))


def test_bfs():
    """Breadth first search a path"""
    graph = create_graph()
    print(graph.breadth_first_search(0, 3))


if __name__ == '__main__':
    test_adjacency_list_graph()
    test_dfs()
    test_bfs()
