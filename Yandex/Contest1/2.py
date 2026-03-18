import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    if n < 0 or m < 0:
        print("-2")
        return

    static = []
    idx = 2
    for _ in range(n):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        x = int(input_data[idx + 2])
        static.append((l, r, x))
        idx += 3

    for _ in range(m):
        q = int(input_data[idx])
        idx += 1

        now = 0
        for l, r, x in static:
            if l <= q <= r:
                if (q - l) % 2 == 0:
                    now += x
                else:
                    now -= x

        print(now)


if __name__ == "__main__":
    solve()
