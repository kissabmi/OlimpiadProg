import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    ptr = 0
    t = int(data[ptr])
    ptr += 1

    results = []
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        a = [int(x) for x in data[ptr : ptr + n]]
        ptr += n

        pm = [0] * n
        cur_m = 0
        for i in range(n):
            if a[i] > cur_m:
                cur_m = a[i]
            pm[i] = cur_m

        pos = [[] for _ in range(n + 1)]
        for i in range(n):
            pos[a[i]].append(i)

        ans = 0
        curr_l = n
        while curr_l > 0:
            m = pm[curr_l - 1]
            idx_list = pos[m]

            low = 0
            high = len(idx_list) - 1
            best = -1
            while low <= high:
                mid = (low + high) // 2
                if idx_list[mid] < curr_l:
                    best = idx_list[mid]
                    low = mid + 1
                else:
                    high = mid - 1

            curr_l = best
            ans += 1

        results.append(str(ans))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
