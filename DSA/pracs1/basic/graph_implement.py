from abc import ABC, abstractmethod

"""abstract method - kind of template"""
class GraphInterface(ABC):
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        super().__init__()
        self.nv = num_vertices

    @abstractmethod
    def add_edge(self, v1: int, v2: int) -> None:
        pass

    @abstractmethod
    def is_adjacent(self, v1: int, v2: int) -> bool:
        pass

    @abstractmethod
    def return_adjacent(self, v: int) -> list[int]:
        pass


class WeightedGraphInterface(GraphInterface):
    @abstractmethod
    def add_edge(self, v1: int, v2: int, w: int) -> None:
        pass


class Graph(GraphInterface):
    def __init__(self, num_vertices: int) -> None:
        self.nv = num_vertices
        # adjancy ls (dict)
        self.adj_ls = {i: [] for i in range(num_vertices)}

    def add_edge(self, v1: int, v2: int) -> None:
        """Add an undirected edge between v1 and v2"""
        self.adj_ls[v1].append(v2)
        self.adj_ls[v2].append(v1)
        return

    def is_adjacent(self, v1: int, v2: int) -> None:
        """Check if v1 and v2 are adjacent"""
        return v2 in self.adj_ls[v1]
    
    def return_adjacent(self, v: int) -> list[int]:
        """Return the list of adjacent vertices of v"""
        return self.adj_ls[v]

class DirectedGraph(GraphInterface):
    def __init__(self, num_vertices: int) -> None:
        self.nv = num_vertices
        # adjancy ls (dict)
        self.adj_ls = {i: [] for i in range(num_vertices)}

    def add_edge(self, v1: int, v2: int) -> None:
        """Add a directed edge from v1 to v2"""
        self.adj_ls[v1].append(v2)
        return
    
    def is_adjacent(self, v1: int, v2: int) -> None:
        """Check if there is a directed edge from v1 to v2"""
        return v2 in self.adj_ls[v1]

    def return_adjacent(self, v: int) -> list[int]:
        """Return the list of adjacent vertices of v"""
        return self.adj_ls[v]



class WeightedGraph(WeightedGraphInterface):
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        # dict of dicts for weighted edges
        self.adj_ls = {i: {} for i in range(num_vertices)}

    def add_edge(self, v1: int, v2: int, w: int) -> None:
        """Add a weighted edge between v1 and v2"""
        self.adj_ls[v1][v2] = w
        # since it's an undirected weighted gh
        self.adj_ls[v2][v1] = w

    def is_adjacent(self, v1: int, v2: int) -> bool:
        """Check if v1 and v2 are adjacent"""
        return v2 in self.adj_ls[v1]

    def return_adjacent(self, v: int) -> list[int]:
        """Return the list of adjacent vertices of v"""
        return list(self.adj_ls[v].keys())

    def get_weight(self, v1: int, v2: int) -> int:
        """Get the weight of the edge between v1 and v2"""
        return self.adj_ls[v1].get(v2, float('inf'))

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    print("Graph adjacency list:", graph.adj_ls)
    print("Is 0 adjacent to 1?", graph.is_adjacent(0, 1))
    print("Adjacent to 1:", graph.return_adjacent(1))

    d_graph = DirectedGraph(5)
    d_graph.add_edge(0, 1)
    d_graph.add_edge(1, 2)
    print("\nDirected Graph adjacency list:", d_graph.adj_ls)
    print("Is 1 adjacent to 2?", d_graph.is_adjacent(1, 2))
    print("Adjacent to 1:", d_graph.return_adjacent(1))

    w_graph = WeightedGraph(5)
    w_graph.add_edge(0, 1, 10)
    w_graph.add_edge(1, 2, 20)
    print("\nWeighted Graph adjacency list:", w_graph.adj_ls)
    print("Weight between 0 and 1:", w_graph.get_weight(0, 1))