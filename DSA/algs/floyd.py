# Replace ___ with your code


def floyd(adj_matrix):
    n = len(adj_matrix)
    dist = [[float('inf')] * n for _ in range(n)]
    pred = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 0 or i == j:
                dist[i][j] = adj_matrix[i][j]
                if i != j:
                    pred[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

def get_path(pred, a, b):
    if pred[a][b] == -1:
        return []
    path = [b]
    while b != a:
        b = pred[a][b]
        path.append(b)
    path.reverse()
    return [str(x) for x in path]

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
short_path = get_path(pred, a, b)

# Output template for test
print(f"A shortest path from {a} to {b} is: {' '.join(short_path)}.")

# from 0 to 5