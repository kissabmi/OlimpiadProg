def solve():
    with open("peacefulsets.in", "r") as f:
        data = f.read().split()

    if not data:
        return

    n = int(data[0])

    # S[i][j] - количество мирных множеств с суммой i и макс элементом <= j
    S = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > i:
                # В сумме i максимальный элемент не может превышать саму сумму i
                S[i][j] = S[i][i]
            elif i == j:
                # Добавляем само число i как единичное множество
                S[i][j] = S[i][j - 1] + 1
            else:
                # Обычный переход: S[i][j-1] плюс варианты, где макс элемент РОВНО j.
                # Если макс элемент j, осталась сумма i - j. И след макс должен быть <= j // 2
                S[i][j] = S[i][j - 1] + S[i - j][j // 2]

    with open("peacefulsets.out", "w") as f:
        f.write(str(S[n][n]) + "\n")

if __name__ == "__main__":
    solve()
