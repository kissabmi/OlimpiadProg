import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    res = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        if n == 1:
            res.append("NO")
            idx += 1
            continue

        counts = {}
        max_f = 0
        total = n * n

        for i in range(idx, idx + total):
            c = data[i]
            counts[c] = counts.get(c, 0) + 1
            if counts[c] > max_f:
                max_f = counts[c]

        if max_f <= total - n:
            res.append("YES")
        else:
            res.append("NO")

        idx += total

    print("\n".join(res))


if __name__ == "__main__":
    solve()
