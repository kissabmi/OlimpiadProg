import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    results = []

    for i in range(1, t + 1):
        s = input_data[i]
        bad_pairs = 0

        for j in range(len(s) - 1):
            if s[j] == s[j + 1]:
                bad_pairs += 1

        if bad_pairs <= 2:
            results.append("YES")
        else:
            results.append("NO")

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
