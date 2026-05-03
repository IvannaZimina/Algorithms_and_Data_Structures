from abc import ABC, abstractmethod


# Base interface for graph classes to enforce a common API.
# If a child class does not override a method, it will raise an error;
# using raise is fine and clearly says "not implemented".
class GraphInterface(ABC):
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        super().__init__()

    @abstractmethod
    def add_edge(self, v1: int, v2: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_adjacent(self, v1: int, v2: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def return_adjacent(self, v: int) -> list[int]:
        raise NotImplementedError


class WeightedGraphInterface(GraphInterface):
    @abstractmethod
    def add_edge(self, v1: int, v2: int, w: int) -> None:
        raise NotImplementedError


class Graph(GraphInterface):
    def __init__(self, num_vertices: int) -> None:
        # graph cannot have 0 or a negative number of vertices
        if num_vertices <= 0:
            raise ValueError("num_vertices must be positive")
        
        # how many vertices are there in the graph
        self._num_vertices = num_vertices

        # for each vertex, a set of neighbors is stored
        self._adjacency: list[set[int]] = [set() for _ in range(num_vertices)]

    def _validate_vertex(self, v: int) -> None:
        # check if the vertex index is valid (between 0 and num_vertices - 1)
        if not 0 <= v < self._num_vertices:
            raise IndexError("vertex out of range")

    # adds an edge in both directions since the graph is undirected
    def add_edge(self, v1: int, v2: int) -> None:
        self._validate_vertex(v1)
        self._validate_vertex(v2)

        # when trying to connect a vertex to itself, the method simply does nothing.
        if v1 == v2:
            return
        
        self._adjacency[v1].add(v2)
        self._adjacency[v2].add(v1)

    # check if v1 anf v2 are neighbors, return True if they are, False otherwise
    def is_adjacent(self, v1: int, v2: int) -> bool:
        self._validate_vertex(v1)
        self._validate_vertex(v2)
        return v2 in self._adjacency[v1]

    # returns a list of neighbors of vertex v, sorted in ascending order
    def return_adjacent(self, v: int) -> list[int]:
        self._validate_vertex(v)
        return sorted(self._adjacency[v])


class DirectedGraph(GraphInterface):
    def __init__(self, num_vertices: int) -> None:
        # check if the number of vertices is positive
        if num_vertices <= 0:
            raise ValueError("num_vertices must be positive")
        
        # store the number of vertices in the graph
        self._num_vertices = num_vertices

        # for each vertex, a set of neighbors is stored;
        # A graph storage structure is created:
        #   list index = node number
        #   set = where to go from this node
        self._adjacency: list[set[int]] = [set() for _ in range(num_vertices)]

    # check if the vertex index is valid (between 0 and num_vertices - 1)
    def _validate_vertex(self, v: int) -> None:
        if not 0 <= v < self._num_vertices:
            raise IndexError("vertex out of range")

    # Adds a directed edge from v1 to v2.
    def add_edge(self, v1: int, v2: int) -> None:
        # both vertices must exist in the graph
        self._validate_vertex(v1)
        self._validate_vertex(v2)

        # check if v1 and v2 are the same vertex
        if v1 == v2:
            return
        
        # Only one direction is added - from v1 you can go to v2
        self._adjacency[v1].add(v2)

    def is_adjacent(self, v1: int, v2: int) -> bool:
        # both vertices must exist in the graph
        self._validate_vertex(v1)
        self._validate_vertex(v2)

        # is v2 among v1's outgoing neighbors
        return v2 in self._adjacency[v1]

    def return_adjacent(self, v: int) -> list[int]:
        self._validate_vertex(v)
        return sorted(self._adjacency[v])

# - the graph has edge weights (numbers)
# - connections between vertices in both directions
# - edge weights are the same in both directions
# - loops are prohibited
class WeightedGraph(WeightedGraphInterface):
    def __init__(self, num_vertices: int) -> None:
        # check if the number of vertices is positive
        if num_vertices <= 0:
            raise ValueError("num_vertices must be positive")
        
        # store the number of vertices in the graph
        self._num_vertices = num_vertices

        # for each vertex, a dictionary of neighbors is stored, where the key is the neighbor and the value is the weight of the edge;
        self._adjacency: list[dict[int, int]] = [dict() for _ in range(num_vertices)]

    def _validate_vertex(self, v: int) -> None:
        if not 0 <= v < self._num_vertices:
            raise IndexError("vertex out of range")

    # add an edge with weight w between v1 and v2;
    # since the graph is undirected, the edge is added in both directions with the same weight
    def add_edge(self, v1: int, v2: int, w: int) -> None:
        self._validate_vertex(v1)
        self._validate_vertex(v2)

        # when trying to connect a vertex to itself, the method simply does nothing.
        if v1 == v2:
            return
        
        # add the edge with weight w in both directions
        self._adjacency[v1][v2] = w
        self._adjacency[v2][v1] = w

    # checks if there is an edge between v1 and v2
    def is_adjacent(self, v1: int, v2: int) -> bool:
        self._validate_vertex(v1)
        self._validate_vertex(v2)
        # is vertex v2 among the neighbors of v1
        return v2 in self._adjacency[v1]

    def return_adjacent(self, v: int) -> list[int]:
        self._validate_vertex(v)
        return sorted(self._adjacency[v].keys())


if __name__ == "__main__":
    graph = Graph(5)
