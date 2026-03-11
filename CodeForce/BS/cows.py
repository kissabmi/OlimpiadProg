def solve():
    with open("cows.in", "r") as f:
        n, k = map(int, f.readline().strip().split())
        coords = [int(x) for x in f.readline().strip().split()]

    def can_place(d):
        count = 1
        last = coords[0]
        for i in range(1, n):
            if coords[i] - last >= d:
                count += 1
                last = coords[i]
                if count >= k:
                    return True
        return False

    lo = 1
    hi = coords[-1] - coords[0]
    ans = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if can_place(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    with open("cows.out", "w") as f:
        f.write(str(ans))


if __name__ == "__main__":
    solve()
