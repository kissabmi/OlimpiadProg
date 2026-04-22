def solve():
    with open("cycle2.in", "r") as f:
        input_data = f.read().split()

    if not input_data:
        return

    N = int(input_data[0])
    M = int(input_data[1])

    adj = [[] for _ in range(N + 1)]
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)

    # Массив цветов для поиска цикла:
    # 0 - белый (не посещали)
    # 1 - серый (в процессе обхода, сейчас в стеке)
    # 2 - черный (полностью обошли)
    color = [0] * (N + 1)

    # Массив предков для восстановления самого цикла
    parent = [-1] * (N + 1)

    # Указатель на следующего соседа для обработки (замена циклу for для итеративного обхода)
    edge_idx = [0] * (N + 1)

    cycle_start = -1
    cycle_end = -1

    # Итеративный обход графа (исключаем рекурсию)
    for i in range(1, N + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1

            while stack:
                u = stack[-1]

                # Если в процессе мы уже нашли цикл, прерываем цикл while
                if cycle_start != -1:
                    break

                # Обрабатываем соседей вершины u
                if edge_idx[u] < len(adj[u]):
                    v = adj[u][edge_idx[u]]
                    edge_idx[u] += 1

                    if color[v] == 0:
                        # Идем вглубь по графу
                        color[v] = 1
                        parent[v] = u
                        stack.append(v)
                    elif color[v] == 1:
                        # Нашли "серого" соседа - это обратное ребро
                        cycle_start = v
                        cycle_end = u
                        break
                else:
                    # Все соседи пройдены, вершина становится черной
                    color[u] = 2
                    stack.pop()

        # Если цикл найден в одной из компонент связности, общий поиск прекращаем
        if cycle_start != -1:
            break

    # Записываем результат и восстанавливаем цикл
    with open("cycle2.out", "w") as f:
        if cycle_start == -1:
            f.write("NO\n")
        else:
            cycle = []
            curr = cycle_end

            # Проходим по ссылкам предков от конца цикла (u) до его начала (v)
            while curr != cycle_start:
                cycle.append(curr)
                curr = parent[curr]
            cycle.append(cycle_start)

            # Поскольку мы разворачивали цикл с конца, переворачиваем список
            cycle.reverse()

            f.write("YES\n")
            f.write(" ".join(map(str, cycle)) + "\n")

if __name__ == "__main__":
    solve()
