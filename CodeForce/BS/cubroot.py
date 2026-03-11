def solve():
    with open("cubroot.in", "r") as f:
        a, b, c, d = map(int, f.readline().strip().split())

    def f(x):
        return a * x**3 + b * x**2 + c * x + d

    root = None

    for xtest in range(-100000, 100001):
        if f(xtest) == 0:
            root = xtest
            break

    if root is None:
        low, high = -1.0, 1.0
        for _ in range(100):
            low_val = f(low)
            high_val = f(high)
            if low_val == 0:
                root = low
                break
            if high_val == 0:
                root = high
                break
            if low_val * high_val < 0:
                break
            low *= 2
            high *= 2

        if root is None:
            for _ in range(200):
                mid = (low + high) / 2.0
                mid_val = f(mid)
                if abs(mid_val) < 1e-12:
                    root = mid
                    break
                if f(low) * mid_val <= 0:
                    high = mid
                else:
                    low = mid
            if root is None:
                root = (low + high) / 2.0

    with open("cubroot.out", "w") as f:
        f.write("{:.6f}\n".format(root))


if __name__ == "__main__":
    solve()
