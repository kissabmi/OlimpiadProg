import sys


def solve():
    input_data = sys.stdin.read().split()

    idx = 0
    t = int(input_data[idx])
    idx += 1

    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1

        a = []
        for _ in range(n):
            a.append(int(input_data[idx]))
            idx += 1

        ans = [0] * n

        for i in range(n):
            count_smaller = 0
            count_larger = 0
            val_i = a[i]

            for j in range(i + 1, n):
                val_j = a[j]
                if val_j < val_i:
                    count_smaller += 1
                elif val_j > val_i:
                    count_larger += 1

            if count_smaller > count_larger:
                ans[i] = count_smaller
            else:
                ans[i] = count_larger

        results.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
