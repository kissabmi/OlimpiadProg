import sys


def solve():
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())

    tests = []
    for _ in range(t):
        line = sys.stdin.readline()
        if not line:
            break
        tests.append(int(line.strip()))

    if not tests:
        return

    max_m = max(tests)

    # пирамидальные числа до max_m
    pyramids = []
    n = 1
    while True:
        val = n * (n + 1) * (n + 2) // 6
        if val > max_m:
            break
        pyramids.append(val)
        n += 1

    dp = [300_001] * (max_m + 1)
    dp[0] = 0

    for p in pyramids:
        for x in range(p, max_m + 1):
            if dp[x - p] + 1 < dp[x]:
                dp[x] = dp[x - p] + 1

    for m in tests:
        print(dp[m])


if __name__ == "__main__":
    solve()
