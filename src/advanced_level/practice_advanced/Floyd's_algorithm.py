# Create a function floyd() with input of adjacency matrix

# Replace ___ with your code


def floyd(adj_matrix):
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

# getting distances and predecessors
# f.e: [1, 2, 3]
dist, pred = floyd(am)

# Calculating shortest path from a to b using dist and pred
___

# Output template for test
print(f"A shortest path from {a} to {b} is: {' '.join(short_path)}.")