def solve():
    with open("ancestor.in", "r") as f:
        input_data = f.read().split()

    if not input_data:
        return

    n = int(input_data[0])

    # Список смежности: для каждой вершины будем хранить список её детей
    adj = [[] for _ in range(n + 1)]
    root = 0

    # Считываем предков для вершин от 1 до n
    for i in range(1, n + 1):
        p = int(input_data[i])
        if p == 0:
            root = i  # Предок 0 означает, что это корень дерева
        else:
            adj[p].append(i)  # Записываем, что i - это ребёнок p

    # вход и выход в вершину
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    timer = 0

    # Итеративный обход в глубину (на стеке) для прохождения лимита памяти
    stack = [root]
    enter = [True] * (n + 1)

    while stack:
        v = stack[-1]

        if enter[v]:
            enter[v] = False
            timer += 1
            tin[v] = timer  # когда входим в вершину

            # добавляем детей в стек
            for u in adj[v]:
                stack.append(u)
        else:
            # когда все дети обработаны, возвращаемся в вершину
            tout[v] = timer  # момент выхода
            stack.pop()

    m = int(input_data[n + 1])
    idx = n + 2

    out = []

    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2

        # a является предком b, если мы вошли в a до b, и вышли из a после b
        if tin[a] <= tin[b] and tout[a] >= tout[b]:
            out.append("1")
        else:
            out.append("0")

    with open("ancestor.out", "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
