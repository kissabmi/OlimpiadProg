def solve():
    with open("bridges.in", "r") as f:
        input_data = f.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    # adj_v хранит соседние вершины, adj_id хранит номера рёбер (1..M)
    adj_v = [[] for _ in range(n + 1)]
    adj_id = [[] for _ in range(n + 1)]

    idx = 2
    for i in range(1, m + 1):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        adj_v[u].append(v)
        adj_id[u].append(i)
        adj_v[v].append(u)
        adj_id[v].append(i)

    tin = [0] * (n + 1)
    fup = [0] * (n + 1)
    timer = 0
    bridges = []

    edge_idx = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)

    # Итеративный обход в глубину для поиска мостов
    for start in range(1, n + 1):
        if tin[start] == 0:
            stack = [start]
            timer += 1
            tin[start] = fup[start] = timer

            while stack:
                u = stack[-1]

                # Если у вершины u еще остались непроверенные соседи
                if edge_idx[u] < len(adj_v[u]):
                    idx_u = edge_idx[u]
                    v = adj_v[u][idx_u]
                    e_idx = adj_id[u][idx_u]
                    edge_idx[u] += 1

                    # Если мы пытаемся пройти по тому же ребру, по которому пришли в u, пропускаем
                    if e_idx == parent_edge[u]:
                        continue

                    if tin[v] != 0:
                        # Если сосед уже посещен, значит это обратное ребро
                        # и мы можем подняться по дереву еще выше
                        if tin[v] < fup[u]:
                            fup[u] = tin[v]
                    else:
                        # Иначе идем исследовать этого соседа
                        parent_edge[v] = e_idx
                        timer += 1
                        tin[v] = fup[v] = timer
                        stack.append(v)
                else:
                    # Все соседи обработаны, вершина завершает работу
                    stack.pop()
                    if stack:
                        p = stack[-1] # p - вершина, в которую мы сейчас вернулись
                        # Передаём предку информацию о том, как высоко мы смогли подняться
                        if fup[u] < fup[p]:
                            fup[p] = fup[u]
                        # Условие моста: если из всего поддерева u нельзя подняться к p или выше
                        if fup[u] > tin[p]:
                            bridges.append(parent_edge[u])

    bridges.sort()

    with open("bridges.out", "w") as f:
        f.write(str(len(bridges)) + "\n")
        if bridges:
            f.write(" ".join(map(str, bridges)) + "\n")

if __name__ == "__main__":
    solve()
