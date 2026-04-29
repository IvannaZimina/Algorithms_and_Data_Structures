# Create a function dijkstra() with input of adjacency matrix

# Replace ___ with your code


def dijkstra(adj_matrix):
    ___

am = [
    [0, 4, 4, 0, 0, 0], 
    [4, 0, 2, 0, 0, 0], 
    [4, 2, 0, 3, 1, 6], 
    [0, 0, 3, 0, 0, 2], 
    [0, 0, 1, 0, 0, 3], 
    [0, 0, 6, 2, 3, 0] 
]

# take Nodes input
a, b = (int(x) for x in input().split())

# getting short path
# f.e: [1, 2, 3]
short_path = dijkstra(am)

# Output template for test
print(f"A shortest path from {a} to {b} is: {' '.join(short_path)}.")