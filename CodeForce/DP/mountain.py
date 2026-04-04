import sys


def main():
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    triangle = []
    idx = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(int(data[idx]))
            idx += 1
        triangle.append(row)

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            # выбираем максимальный путь из левого нижнего и правого нижнего элемента
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    max_score = triangle[0][0]

    print(max_score)


if __name__ == "__main__":
    main()
