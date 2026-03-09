def solve():

    with open("lepus.in", "r") as f:
        n = int(f.readline().strip())
        path = f.readline().strip()

    dp = [-1] * n

    dp[0] = 0

    for i in range(1, n):
        if path[i] == "w":
            continue

        max_prev = -1
        for step in (1, 3, 5):
            if (i - step >= 0) and (dp[i - step] != -1):
                max_prev = max(max_prev, dp[i - step])

        if max_prev != -1:
            grass = 1 if path[i] == '"' else 0
            dp[i] = max_prev + grass

    with open("lepus.out", "w") as f:
        f.write(str(dp[n - 1]) + "\n")


if __name__ == "__main__":
    solve()
