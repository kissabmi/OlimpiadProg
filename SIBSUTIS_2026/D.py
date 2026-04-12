import sys
import math


def solve():
    n = int(sys.stdin.readline().strip())

    if n <= 10000:  # это вот мой имбовый метод
        massiv = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                if massiv[j] == 0 or massiv[j] == 1:
                    massiv[j] = 2
                elif massiv[j] == 2:
                    massiv[j] = 1

        count = 0
        for j in range(1, n + 1):
            if massiv[j] == 2:
                count += 1

        print(count)
    else:
        result = int(math.sqrt(n))
        print(result)


if __name__ == "__main__":
    solve()
