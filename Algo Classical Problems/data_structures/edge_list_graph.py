"""Edge list representation of a graph"""

class EdgeListGraph:
    """Edge list graph is a two dimensional list of vertex and edges"""

    def __init__(self):
        self.__edge_list = []

    def __str__(self):
        return str(self.__edge_list)

    def insert_edge(self, vertex_start, vertex_end) -> bool:
        """Insert an edge into the graph"""
        self.__edge_list.append([vertex_start, vertex_end])
        return True


def test_edge_list():
    """Basic test implementation"""
    graph = EdgeListGraph()

    graph.insert_edge(0, 1)
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 3)

    print(graph)

if __name__ == '__main__':
    test_edge_list()
