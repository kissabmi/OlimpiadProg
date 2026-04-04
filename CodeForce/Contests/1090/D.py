import sys


def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        ans = ["1"]
        for i in range(2, n + 1):
            val = (2 * i - 3) * (2 * i - 1)
            ans.append(str(val))
        print(" ".join(ans))


if __name__ == "__main__":
    solve()
