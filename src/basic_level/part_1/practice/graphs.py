from abc import ABC, abstractmethod


class GraphInterface(ABC):
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        super().__init__()

    @abstractmethod
    def add_edge(v1: int, v2: int) -> None:
        pass

    @abstractmethod
    def is_adjacent(v1: int, v2: int) -> bool:
        pass

    @abstractmethod
    def return_adjacent(v: int) -> list[int]:
        pass


class WeightedGraphInterface(GraphInterface):
    @abstractmethod
    def add_edge(v1: int, v2: int, w: int) -> None:
        pass


class Graph(GraphInterface):
    pass


class DirectedGraph(GraphInterface):
    pass


class WeightedGraph(WeightedGraphInterface):
    pass


if __name__ == "__main__":
    graph = Graph(5)
