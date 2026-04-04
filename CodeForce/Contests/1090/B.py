import sys


def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a = list(map(int, sys.stdin.readline().split()))
        ans = 2 * max(a) - sum(a)
        print(ans)


if __name__ == "__main__":
    solve()
