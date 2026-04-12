# нод двух чисел
def nod(a, b):
    while b != 0:
        ostatok = a % b
        a = b
        b = ostatok
    return a


def solve():
    n = int(input())

    nd = nod(n, 2026)

    k = 2026 // nd

    print(k)


if __name__ == "__main__":
    solve()
