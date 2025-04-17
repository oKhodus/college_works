# Replace ___ with your code


def kruskal(adj_list):
    total = 0
    parent = {}

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        parent[find(u)] = find(v)

    edges = []
    for u in adj_list:
        for v, w in adj_list[u].items():
            if (v, u, w) not in edges:
                edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])

    for node in adj_list:
        parent[node] = node

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            total += w

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
