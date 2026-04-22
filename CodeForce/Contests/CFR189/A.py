import sys

def solve():
    # Читаем количество наборов данных
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    pointer = 1
    results = []

    for _ in range(t):
        x = int(input_data[pointer])
        y = int(input_data[pointer + 1])
        pointer += 2

        # Если между x и y есть хотя бы два шага по x,
        # то z = y - x всегда подойдет.
        if y > 2 * x:
            results.append("YES")
        else:
            results.append("NO")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
