import sys
import math


def solve():
    data = sys.stdin.readline().split()
    d = int(data[0])
    h = int(data[1])
    w = int(data[2])
    k = int(data[3])

    if 2 * d > k:
        print(-1)
        return

    if w == 0:
        print(0)
        return

    eps = 1e-9

    theta_shield_rad = math.atan(w / d)
    y_house_at_shield_angle = 2 * d * math.tan(theta_shield_rad)

    if y_house_at_shield_angle <= h + eps:
        distance = 2 * d / math.cos(theta_shield_rad)
        if distance <= k + eps:
            print(f"{math.degrees(theta_shield_rad):.4f}")
            return

    if 2 * d < k - eps:
        theta_max_rad = math.acos(2 * d / k)
        y_shield_at_max = d * math.tan(theta_max_rad)
        y_house_at_max = 2 * d * math.tan(theta_max_rad)

        if y_shield_at_max > w - eps and y_house_at_max >= h - eps:
            print(f"{math.degrees(theta_max_rad):.4f}")
            return

    print(-1)


if __name__ == "__main__":
    solve()
