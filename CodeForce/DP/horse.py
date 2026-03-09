def solve():
    with open("knight.in", "r") as f:
        n, m = map(int, f.read().split())

    dp = [[0] * m for _ in range(n)]

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            # если могли прийти ходом "2 вниз, 1 вправо" (значит пришли из i-2, j-1)
            if i - 2 >= 0 and j - 1 >= 0:
                dp[i][j] += dp[i - 2][j - 1]

            # если могли прийти ходом "1 вниз, 2 вправо" (значит пришли из i-1, j-2)
            if i - 1 >= 0 and j - 2 >= 0:
                dp[i][j] += dp[i - 1][j - 2]

    # в итоге сумма всех способов попасть в клетку (n-1, m-1) будет нашим ответом
    ans = dp[n - 1][m - 1]

    with open("knight.out", "w") as f:
        f.write(str(ans))


if __name__ == "__main__":
    solve()
