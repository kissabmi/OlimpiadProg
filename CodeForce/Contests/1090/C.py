import sys


def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        ans = []
        for i in range(n):
            ans.append(str(i + 1))
            ans.append(str(n + 1 + 2 * i))
            ans.append(str(n + 2 + 2 * i))
        print(" ".join(ans))


if __name__ == "__main__":
    solve()
