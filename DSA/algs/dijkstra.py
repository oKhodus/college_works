# Replace ___ with your code


def dijkstra(adj_matrix):
    n = len(adj_matrix)
    dist = [float('inf')] * n
    prev = [-1] * n
    visited = [False] * n
    dist[a] = 0

    for _ in range(n):
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if adj_matrix[u][v] > 0 and not visited[v]:
                alt = dist[u] + adj_matrix[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    # восстановление пути
    path = []
    curr = b
    while curr != -1:
        path.append(str(curr))
        curr = prev[curr]
    return path[::-1] if dist[b] != float('inf') else []

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