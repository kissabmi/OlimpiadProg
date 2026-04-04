import sys


def solve():
    n = int(sys.stdin.readline())

    if n == 0:
        print(1)
        return

    # для n = 1 у нас есть ровно по одной строке,
    c0 = 1  # количество строк, оканчивающихся на 0
    c1 = 1  # количество строк, оканчивающихся на 1
    c2 = 1  # количество строк, оканчивающихся на 2

    # начинаем строить строки от 2 до n
    for i in range(1, n):

        new_c0 = c0 + c1 + c2
        new_c1 = c1 + c2
        new_c2 = c0 + c1 + c2

        c0, c1, c2 = new_c0, new_c1, new_c2

    print(c0 + c1 + c2)


if __name__ == "__main__":
    solve()
