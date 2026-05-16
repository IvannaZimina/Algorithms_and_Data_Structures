from abc import ABC, abstractmethod


class GraphInterface(ABC):
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        super().__init__()

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
        if num_vertices < 0:
            raise ValueError("num_vertices must be non-negative")
        
        self.num_vertices = num_vertices

        # adjacency list: each entry is a list of neighbor vertex indices
        # start list: self.adj = [[], [], [], ...]
        self.adj: list[list[int]] = [[] for _ in range(num_vertices)]

    # helper method to check if vertex index is valid
    def _check_vertex(self, v: int) -> None:
        if v < 0 or v >= self.num_vertices:
            raise IndexError(f"vertex {v} is out of range")

    # add an undirected edge between v1 and v2
    def add_edge(self, v1: int, v2: int) -> None:
        self._check_vertex(v1)
        self._check_vertex(v2)

        # example: add_edge(0, 1)
        # 1) if vertex 1 is not already in the adjacency list of vertex 0, add it
        if v2 not in self.adj[v1]:
            self.adj[v1].append(v2)

        # 2) since this is an undirected graph, also add vertex 0 to the adjacency list of vertex 1 if it's not already there
        if v1 not in self.adj[v2]:
            self.adj[v2].append(v1)

    # check if two vertices are adjacent
    def is_adjacent(self, v1: int, v2: int) -> bool:
        self._check_vertex(v1)
        self._check_vertex(v2)
        return v2 in self.adj[v1]

    # return a list of all vertices it is connected to
    def return_adjacent(self, v: int) -> list[int]:
        self._check_vertex(v)
        return list(self.adj[v])

    def __repr__(self) -> str:
        return f"Graph(num_vertices={self.num_vertices}, adj={self.adj})"


class DirectedGraph(GraphInterface):
    def __init__(self, num_vertices: int) -> None:
        if num_vertices < 0:
            raise ValueError("num_vertices must be non-negative")
        self.num_vertices = num_vertices

        # start list: self.adj = [[], [], [], ...]
        self.adj: list[list[int]] = [[] for _ in range(num_vertices)]

    def _check_vertex(self, v: int) -> None:
        if v < 0 or v >= self.num_vertices:
            raise IndexError(f"vertex {v} is out of range")

    def add_edge(self, v1: int, v2: int) -> None:
        self._check_vertex(v1)
        self._check_vertex(v2)

        # as it is a directed graph, we only add v2 to the adjacency list of v1, not the other way around
        if v2 not in self.adj[v1]:
            self.adj[v1].append(v2)

    def is_adjacent(self, v1: int, v2: int) -> bool:
        self._check_vertex(v1)
        self._check_vertex(v2)
        return v2 in self.adj[v1]

    def return_adjacent(self, v: int) -> list[int]:
        self._check_vertex(v)
        return list(self.adj[v])

    def __repr__(self) -> str:
        return f"DirectedGraph(num_vertices={self.num_vertices}, adj={self.adj})"


class WeightedGraph(WeightedGraphInterface):
    def __init__(self, num_vertices: int) -> None:
        if num_vertices < 0:
            raise ValueError("num_vertices must be non-negative")
        self.num_vertices = num_vertices

        # adjacency list: each entry is a list of (neighbor, weight)
        # start list: self.adj = [(neighbor, weight), (neighbor, weight), ...]
        # example: adj[0] = [(1, 5), (2, 10)] -> 0 → 1 (weight 5), 0 → 2 (weight 10)
        self.adj: list[list[tuple[int, int]]] = [[] for _ in range(num_vertices)]

    def _check_vertex(self, v: int) -> None:
        if v < 0 or v >= self.num_vertices:
            raise IndexError(f"vertex {v} is out of range")

    def add_edge(self, v1: int, v2: int, w: int) -> None:
        self._check_vertex(v1)
        self._check_vertex(v2)

        # Is vertex v2 among the neighbors of vertex v1?
        # for nb, _ in adj[v1] - loop through all neighbors
        # nb == v2 - check: is this the right neighbor?
        # any(...) - is there at least one such neighbor
        if not any(nb == v2 for nb, _ in self.adj[v1]):
            self.adj[v1].append((v2, w))

        # Is there a vertex v2 among the neighbors of v1?
        if not any(nb == v1 for nb, _ in self.adj[v2]):
            self.adj[v2].append((v1, w))

        # example:
        # wg = WeightedGraph(4)
        # adj = [
        #   [],   # 0
        #   [],   # 1
        #   [],   # 2
        #   []    # 3
        # ]

        # 1) 
        # adj[0].append((1, 5))
        # adj[1].append((0, 5))

        # adj = [
        #   [(1, 5)],   # 0
        #   [(0, 5)],   # 1
        #   [],         # 2
        #   []          # 3
        # ]

        # 0 ----(5)---- 1

        # 2) 
        # adj[0].append((2, 7))
        # adj[2].append((0, 7))

        # adj = [
        #   [(1, 5), (2, 7)],  # 0
        #   [(0, 5)],          # 1
        #   [(0, 7)],          # 2
        #   []
        # ]

        #      (5)
        # 0 -------- 1
        #  \
        #   \
        #   (7)
        #     \
        #      2

        # 3)
        # adj[1].append((3, 4))
        # adj[3].append((1, 4))

        # adj = [
        #     [(1, 5), (2, 7)],   # 0 - between 0 and 1 is weight 5, between 0 and 2 is weight 7
        #     [(0, 5), (3, 4)],   # 1 - between 1 and 0 is weight 5, between 1 and 3 is weight 4
        #     [(0, 7)],           # 2 - between 2 and 0 is weight 7
        #     [(1, 4)]            # 3 - between 3 and 1 is weight 4
        # ]

        #      (5)
        # 0 -------- 1
        #  \         |
        #   \        |
        #   (7)     (4)
        #     \      |
        #      2     3

    def is_adjacent(self, v1: int, v2: int) -> bool:
        self._check_vertex(v1)
        self._check_vertex(v2)
        return any(nb == v2 for nb, _ in self.adj[v1])

    def return_adjacent(self, v: int) -> list[int]:
        self._check_vertex(v)
        # return neighbors without weights to satisfy interface
        return [nb for nb, _ in self.adj[v]]

    def return_adjacent_with_weights(self, v: int) -> list[tuple[int, int]]:
        self._check_vertex(v)
        return list(self.adj[v])

    def __repr__(self) -> str:
        return f"WeightedGraph(num_vertices={self.num_vertices}, adj={self.adj})"


if __name__ == "__main__":
    # small usage demo
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(3, 4)
    print(graph)

    d = DirectedGraph(4)
    d.add_edge(0, 1)
    d.add_edge(0, 2)
    print(d)

    wg = WeightedGraph(4)
    wg.add_edge(0, 1, 5)
    wg.add_edge(1, 2, 7)
    print(wg)

# ===== output =====
# Graph(num_vertices=5, adj=[[1, 2], [0], [0], [4], [3]])
# DirectedGraph(num_vertices=4, adj=[[1, 2], [], [], []])
# WeightedGraph(num_vertices=4, adj=[[(1, 5)], [(0, 5), (2, 7)], [(1, 7)], []])