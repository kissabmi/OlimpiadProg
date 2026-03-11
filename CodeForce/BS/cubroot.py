def solve():
    with open("cubroot.in", "r") as f:
        a, b, c, d = map(float, f.readline().strip().split())

    def f(x):
        return a * x**3 + b * x**2 + c * x + d

    def f_prime(x):
        return 3 * a * x**2 + 2 * b * x + c

    x = 0.0
    if abs(f(x)) < 1e-18:
        root = x
    else:
        for _ in range(10000):
            if abs(f_prime(x)) < 1e-18:
                break
            x = x - f(x) / f_prime(x)
            if abs(f(x)) < 1e-18:
                break

    root = x

    with open("cubroot.out", "w") as f:
        f.write(f"{root:.6f}\n")


if __name__ == "__main__":
    solve()
