import math


def solve():
    with open("forest.in", "r") as f:
        line1 = f.readline().split()
        if not line1:
            return
        vp, vf = map(int, line1)
        line2 = f.readline().split()
        if not line2:
            return
        a = float(line2[0])

    def derivative(x):
        term1 = x / (vp * math.sqrt(x**2 + (1 - a) ** 2))
        term2 = (1 - x) / (vf * math.sqrt((1 - x) ** 2 + a**2))
        return term1 - term2

    low = 0.0
    high = 1.0

    for _ in range(100):
        mid = (low + high) / 2.0
        if derivative(mid) < 0:
            low = mid
        else:
            high = mid

    with open("forest.out", "w") as f:
        f.write("{:.9f}\n".format(high))


if __name__ == "__main__":
    solve()
