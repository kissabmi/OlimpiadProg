import sys


def solve():
    lists = list(map(int, sys.stdin.readline().split()))
    print(lists)
    line1 = sys.stdin.readline().split()
    n, m = int(line1[0]), int(line1[1])
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip())

    count = 0

    for i in range(n):
        for j in range(m):
            if j + 1 < m:
                if lines[i][j] == "." and lines[i][j + 1] == ".":
                    count += 1
            if i + 1 < n:
                if lines[i][j] == "." and lines[i + 1][j] == ".":
                    count += 1

    print(count)


if __name__ == "__main__":
    solve()
