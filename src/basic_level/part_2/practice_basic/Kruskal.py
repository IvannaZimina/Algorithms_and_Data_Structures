# Create a function kruskal() with input of adjacency list

# Replace ___ with your code


def kruskal(adj_list):
    total = 0
    ___
    print(f"Total spanning tree weight is {total}")


graph = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2},
    'C': {'A': 4, 'B': 2, 'D': 3, 'E': 1, 'F': 6},
    'D': {'C': 3, 'F': 2},
    'E': {'C': 1, 'F': 3},
    'F': {'C': 6, 'D': 2, 'E': 3},
}

# calculation total
kruskal(graph)
