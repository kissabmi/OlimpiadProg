import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])

    # яма не образуется
    if n < 3:
        print(0)
        return

    y = []
    for i in range(1, n + 1):
        y.append(int(data[i]))
    # левые максимумы для каждой точки
    l_max = [0] * n
    current_max = 0
    for i in range(n):
        if y[i] > current_max:
            current_max = y[i]
        l_max[i] = current_max

    # правые максимумы для каждой точки (оба максимума чтобы понять куда пойдет вода)
    r_max = [0] * n
    current_max = 0
    for i in range(n - 1, -1, -1):
        if y[i] > current_max:
            current_max = y[i]
        r_max[i] = current_max

    max_h = 0
    for i in range(n):
        water_level = min(
            l_max[i], r_max[i]
        )  # тут мы понимаем куда подет вода и это и будет её высота крче

        depth = (
            water_level - y[i]
        )  # глубина это разница между уровнем воды и высотой земли в этой точке

        if depth > max_h:
            max_h = depth

    print(max_h)


if __name__ == "__main__":
    solve()
