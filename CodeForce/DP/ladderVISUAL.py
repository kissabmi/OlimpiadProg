import time


def visualize_ladder():
    a = [0, 5, -3, 2, 4, -5, -2, 6, 1, -4, 3, -1, 7]
    n = len(a) - 1

    dp = [None] * (n + 1)

    dp[0] = 0
    dp[1] = a[1]

    print("=== ВИЗУАЛИЗАЦИЯ DP: ЛЕСЕНКА ===\n")
    print(f"Ступеньки (a):  {a}")
    print(f"Начальный DP:   {dp}\n")
    print("-" * 50)
    time.sleep(1)

    for i in range(2, n + 1):
        print(f"▶ ШАГ {i}: Стоим перед ступенькой {i}. Значение на ней: {a[i]}")

        jump_1 = dp[i - 1]

        jump_2 = dp[i - 2]

        print(f"   Откуда мы могли сюда прыгнуть?")
        print(f"   1) Со ступеньки {i-1} (там мы накопили {jump_1})")
        print(f"   2) Со ступеньки {i-2} (там мы накопили {jump_2})")

        if jump_1 >= jump_2:
            best_prev = jump_1
            choice = i - 1
            print(
                f"   -> Выгоднее прыгнуть со ступеньки {choice} ({jump_1} >= {jump_2})"
            )
        else:
            best_prev = jump_2
            choice = i - 2
            print(
                f"   -> Выгоднее перепрыгнуть со ступеньки {choice} ({jump_2} > {jump_1})"
            )

        dp[i] = a[i] + best_prev
        print(
            f"   [!] DP[{i}] = {a[i]} (текущая) + {best_prev} (лучшая прошлая) = {dp[i]}"
        )

        dp_visual = [str(x) if x is not None else "?" for x in dp]
        print(f"   Текущий массив DP: {dp_visual}")
        print("-" * 50)

    print("\n=== ИТОГ ===")
    print(f"Максимальная сумма на вершине ({n}-я ступенька): {dp[n]}")

    path = []
    curr = n
    while curr > 0:
        path.append(curr)
        if curr == 1:
            break
        if dp[curr] == a[curr] + dp[curr - 1]:
            curr -= 1
        else:
            curr -= 2

    path.append(0)
    path.reverse()

    print(f"Идеальный маршрут по ступенькам: {path}")


if __name__ == "__main__":
    visualize_ladder()
