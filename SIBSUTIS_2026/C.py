import sys


def solve():
    data = sys.stdin.readline().split()
    n = int(data[0])
    m = int(data[1])

    result = min(n + m, 2 * min(n, m) + 1)

    print(result)


if __name__ == "__main__":
    solve()
