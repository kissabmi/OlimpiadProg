def solve():
    a = []
    with open("king2.in", "r") as f:
        for _ in range(8):
            row = list(map(int, f.readline().split()))
            a.append(row)

    # инвертируем: ввод идёт сверху вниз, а король идёт снизу вверх
    a = a[::-1]

    INF = 10**9
    dp = [[INF] * 8 for _ in range(8)]

    dp[0][0] = a[0][0]  # старт

    for i in range(1, 8):
        dp[i][0] = dp[i - 1][0] + a[i][0]

    for j in range(1, 8):
        dp[0][j] = dp[0][j - 1] + a[0][j]

    # остальные клетки
    for i in range(1, 8):
        for j in range(1, 8):
            dp[i][j] = a[i][j] + min(
                dp[i - 1][j],  # снизу
                dp[i][j - 1],  # слева
                dp[i - 1][j - 1],  # по диагонали
            )

    with open("king2.out", "w") as f:
        f.write(str(dp[7][7]))


if __name__ == "__main__":
    solve()
