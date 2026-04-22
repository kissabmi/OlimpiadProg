import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    pointer = 1
    results = []

    for _ in range(t):
        n = int(input_data[pointer])
        r1 = input_data[pointer + 1]
        r2 = input_data[pointer + 2]
        pointer += 3

        dp = [0] * (n + 1)

        dp[1] = 1 if r1[0] != r2[0] else 0

        for i in range(2, n + 1):
            cost_v = 1 if r1[i - 1] != r2[i - 1] else 0

            cost_h = 0
            if r1[i - 2] != r1[i - 1]:
                cost_h += 1
            if r2[i - 2] != r2[i - 1]:
                cost_h += 1

            dp[i] = min(dp[i - 1] + cost_v, dp[i - 2] + cost_h)

        results.append(str(dp[n]))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
