import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])

    bad_rows = [False] * (n + 1)
    bad_cols = [False] * (n + 1)

    idx = 2
    for _ in range(m):
        r = int(data[idx])
        c = int(data[idx + 1])
        bad_rows[r] = True
        bad_cols[c] = True
        idx += 2

    ans = 0

    for i in range(2, n):
        if not bad_rows[i]:
            ans += 1

    for i in range(2, n):
        if not bad_cols[i]:
            ans += 1

    # единственное исключение: точный центр доски
    if n % 2 == 1:
        mid = (n + 1) // 2
        # пересчитали на 1 больше, так как фишки в центре неизбежно столкнутся.
        if not bad_rows[mid] and not bad_cols[mid]:
            ans -= 1

    print(ans)


if __name__ == "__main__":
    solve()
