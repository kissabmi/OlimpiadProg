import sys

sys.setrecursionlimit(20000)


class item:
    def __init__(self, n):
        self._data = [[] for _ in range(n + 1)]

    def append(self, first, second):
        self._data[first].append(second)

    def __getitem__(self, index):
        return self._data[index]


def solve():
    with open("longpath.in", "r") as f:
        raw_data = f.read().split()

    if not raw_data:
        return

    n = int(raw_data[0])
    m = int(raw_data[1])

    data = item(n)

    idx = 2
    for _ in range(m):
        first = int(raw_data[idx])
        second = int(raw_data[idx + 1])
        data.append(first, second)
        idx += 2

    memo = [-1] * (n + 1)

    def dfs(node):
        # если мы уже считали для этой вершины
        if memo[node] != -1:
            return memo[node]

        max_len = 0
        # сморим всех соседей
        for neighbor in data[node]:
            # длина равна 1 (текущая дуга) + самый длинный путь от соседа
            max_len = max(max_len, 1 + dfs(neighbor))

        memo[node] = max_len
        return max_len

    # Ищем глобальный максимальный путь, пробуя стартовать из каждой вершины
    global_max_path = 0
    for i in range(1, n + 1):
        global_max_path = max(global_max_path, dfs(i))

    with open("longpath.out", "w") as f:
        f.write(str(global_max_path) + "\n")


if __name__ == "__main__":
    solve()
