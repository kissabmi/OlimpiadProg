import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    companies = [int(x) for x in input_data[1:]]

    if n == 1:
        print(1)
        return

    win = [False] * n

    static = [(companies[i], i) for i in range(n)]
    static.sort(key=lambda x: x[0])

    curr = [0] * n
    curr[0] = static[0][0]
    for i in range(1, n):
        curr[i] = curr[i - 1] + static[i][0]

    count = -1
    for i in range(n - 1):
        if curr[i] <= static[i + 1][0]:
            count = i

    min_val = static[0][0]

    for i in range(n):
        if static[i][0] > min_val and i > count:
            win[static[i][1]] = True

    ans = ["1" if w else "0" for w in win]
    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    solve()
