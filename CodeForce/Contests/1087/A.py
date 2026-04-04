import sys


def solve():
    input_data = sys.stdin.read().split()

    i = 0
    t = int(input_data[i])
    i += 1

    results = []
    for _ in range(t):
        n = int(input_data[i])
        c = int(input_data[i + 1])
        k = int(input_data[i + 2])
        i += 3

        a = []
        for _ in range(n):
            a.append(int(input_data[i]))
            i += 1

        a.sort()

        for monster_power in a:
            if monster_power <= c:
                can_add = min(k, c - monster_power)

                c += monster_power + can_add

                k -= can_add

        results.append(str(c))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
