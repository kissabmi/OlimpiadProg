import sys
from collections import deque


def solve():
    lines = sys.stdin.read().strip().split("\n")

    n, k = map(int, lines[0].split())
    artifacts = [0] + list(map(int, lines[1].split()))

    graph = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        u, v = map(int, lines[i].split())
        graph[u].append(v)
        graph[v].append(u)

    type1_vertices = []
    type2_vertices = []

    for i in range(1, n + 1):
        if artifacts[i] == 1:
            type1_vertices.append(i)
        elif artifacts[i] == 2:
            type2_vertices.append(i)

    if k >= 1 and not type1_vertices:
        print(-1)
        return
    if k >= 2 and not type2_vertices:
        print(-1)
        return

    if k == 1:
        print(0)
        return

    dist = [-1] * (n + 1)
    queue = deque()

    for v1 in type1_vertices:
        dist[v1] = 0
        queue.append(v1)

    # BFS
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[v] + 1
                queue.append(neighbor)

    # минимальное расстояние до вершин типа 2
    min_distance = 10**18
    for v2 in type2_vertices:
        min_distance = min(min_distance, dist[v2])

    print(min_distance)


if __name__ == "__main__":
    solve()
