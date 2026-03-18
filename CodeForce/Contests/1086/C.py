import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    t_cases = int(data[0])
    curr = 1
    results = []

    for _ in range(t_cases):
        n = int(data[curr])
        curr += 1

        c_vals = []
        p_vals = []
        for i in range(n):
            c_vals.append(float(data[curr]))
            p_vals.append(float(data[curr + 1]))
            curr += 2

        dp_val = 0.0
        for i in range(n - 1, -1, -1):
            option_do = c_vals[i] + (1.0 - p_vals[i] / 100.0) * dp_val
            if option_do > dp_val:
                dp_val = option_do

        results.append(f"{dp_val:.10f}")

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
