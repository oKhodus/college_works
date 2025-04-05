from abc import ABC, abstractmethod


class WeightedGraphInterface(ABC):
    """Represents abstract class which defines interface weighted graph"""

    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        """Initialize the graph with a fixed number of vertices

        Args:
            num_vertices (int): The given value of vertices
        """
        super().__init__()

    @abstractmethod
    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """Sets undirected weighted edge between two given vertices

        Args:
            vertex1 (int): The first given vertex
            vertex2 (int): The second given vertex
            weight (int): The weight of the edge
        """
        pass

    @abstractmethod
    def is_adjacent(self, vertex1: int, vertex2: int) -> bool:
        """Checks if given v2 is adjacent to given v1

        Args:
            vertex1 (int): The first given vertex
            vertex2 (int): The second given vertex
        """
        pass

    @abstractmethod
    def return_adjacent(self, vertex: int) -> list[tuple[int, int]]:
        """Returns adjacent vertices to given vertex

        Args:
            vertex (int): The given vertex
        """
        pass

    @abstractmethod
    def get_path_weight(self, *path) -> int:
        """Traverse a path and calculates total weight

        Returns:
            int: -1 if there is no such a path in graph else total weight of path
        """
        pass


class WeightedGraph(WeightedGraphInterface):
    """Represents weighted graph"""

    def __init__(self, num_vertices: int) -> None:
        """Initializes weighted graph with finite given number of vertices."""
        super().__init__(num_vertices)
        self.graph: dict = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """Sets undirected weighted edge between v1 and v2

        The method sets a new undirected weighted edge and removes an old edge from the graph
        if between given vertices is already edge.

        Args:
            vertex1 (int): The first given vertex
            vertex2 (int): The second given vertex
            weight (int): The weight of the edge between v1 and v2

        Returns:
            None: If the v1 or the v2 is not in the graph.
        """
        try:
            self.check_miss_vert(vertex1, vertex2)
        except KeyError:
            # raise Exception if does not exist in the graph
            print(str(KeyError))
            return

        existing_edge = next(
            (edge for edge in self.graph[vertex1] if edge[0] == vertex2), None
        )
        if existing_edge:
            self.graph[vertex1].remove(existing_edge)
            self.graph[vertex2].remove((vertex1, existing_edge[1]))

        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    def is_adjacent(self, vertex1: int, vertex2: int) -> bool | None:
        """Checks that v2 is adjacent to v1

        Args:
            vertex1 (int): The first given vertex
            vertex2 (int): The second given vertex

        Returns:
            bool: True if v2 is adjacent to v1 else will be False
            None: If the v1 or v2 isn't in graph
        """
        try:
            self.check_miss_vert(vertex1, vertex2)
        except KeyError:
            # raise Exception if does not exist in the graph
            print(str(KeyError))
            return

        return any(neighbour == vertex2 for neighbour, _ in self.graph.get(vertex1, []))

    def return_adjacent(self, vertex: int) -> list[tuple[int, int]] | None:
        """Returns all adjacent vertices to given vertex

        Args:
            vertex (int): The given vertex to get adjacent vertices from it

        Returns:
            list[tuple[int, int]]: Adjacent vertices with their weight to vertex
            None: If given vertex isn't in graph
        """
        try:
            self.check_miss_vert(vertex)
        except KeyError:
            # raise Exception if does not exist in graph
            print(str(KeyError))
            return

        return self.graph[vertex]

    def get_path_weight(self, *path: int) -> int | None:
        """Calculates the total weight of a given path in graph

        The func going through given sequence of vertices and sums up the weights
        of edges connecting two (current and next) vertices in the path. If at any point
        an edge does not exist between two (current and next) vertices - the method will returns -1

        Args:
            path (int): A sequence of vertex id's representing path

        Returns:
            int: The total weight of the path if it exists, otherwise -1.
            None: If vertex from the given path is not in the graph.
        """
        try:
            self.check_miss_vert(*path)
        except KeyError:
            # raise Exception if vertexes does not exist in the graph
            print(str(KeyError))
            return
        # store total weight of the path
        total_path_weight = 0
        # going through the path - from fisrt to beforelast vertex
        for i in range(len(path) - 1):
            # get current and next vertices in path
            vertex1, vertex2 = path[i], path[i + 1]
            # trying to find existing edge btw v1 and v2 in graph
            existing_edge = next(
                (edge for edge in self.graph[vertex1] if edge[0] == vertex2), None
            )
            # if edge exists *- add his weight to total
            if existing_edge:
                total_path_weight += existing_edge[1]
            # if no edge exists btw vertices *- return -1 (path isn't valid)
            else:
                return -1
        return total_path_weight

    def check_miss_vert(self, *vertices: int) -> None:
        """Checks if given vertex or vertices aren't in graph

        Args:
            vertices (int): Vertex or vertices to check that the're exist in graph

        Raises:
            KeyError: If given vertex or vertices isn't in graph

        """
        # make ls of vertices that are missing from graph
        miss_vert = [vertex for vertex in vertices if vertex not in self.graph]

        # if there are missing vertices - will raise a KeyError
        if miss_vert:
            # joins missing vertices into str to display in the error message
            miss_vert_repr = ", ".join(map(str, miss_vert))
            raise KeyError(
                f"There {'is' if len(miss_vert) == 1 else 'are'} no {miss_vert_repr} vertex/vertices in graph with {len(self.graph)} vertices"
            )


if __name__ == "__main__":
    # prompt for num of vertices in graph
    num_vertices = int(input("Enter the number of vertices: "))
    graph = WeightedGraph(num_vertices=num_vertices)

    # prompt for num of edges to add
    num_edges = int(input("Enter the number of edges: "))

    # add edges to the graph
    for i in range(num_edges):
        # ask user to input the edge (two vertices and a weight)
        v1, v2, w = map(
            int, input(f"Enter edge {i+1} (vertex1 vertex2 weight): ").split()
        )
        graph.add_edge(v1, v2, w)

    path = list(
        map(int, input("Enter the path (vertices separated by spaces): ").split())
    )
    print(graph.get_path_weight(*path))

"""
Enter the number of vertices: 5
Enter the number of edges: 2
Enter edge 1 (vertex1 vertex2 weight): 1 2 15
Enter edge 2 (vertex1 vertex2 weight): 2 3 13
Enter the path (vertices separated by spaces): 1 2 3
----> 28


Enter the number of vertices: 4
Enter the number of edges: 3
Enter edge 1 (vertex1 vertex2 weight): 1 3 5
Enter edge 2 (vertex1 vertex2 weight): 2 3 7
Enter edge 3 (vertex1 vertex2 weight): 4 1 2
Enter the path (vertices separated by spaces): 1 3 4
----> 7


Enter the number of vertices: 6
Enter the number of edges: 4
Enter edge 1 (vertex1 vertex2 weight): 1 2 10
Enter edge 2 (vertex1 vertex2 weight): 2 3 20
Enter edge 3 (vertex1 vertex2 weight): 3 4 30
Enter edge 4 (vertex1 vertex2 weight): 4 5 40
Enter the path (vertices separated by spaces): 1 2 3 4 5
-------> 100
"""
