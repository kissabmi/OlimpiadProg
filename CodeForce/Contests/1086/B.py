import sys


def solve():
    d = sys.stdin.read().split()
    if not d:
        return

    t = int(d[0])
    idx = 1
    res = []

    for _ in range(t):
        n = int(d[idx])
        k = int(d[idx + 1])
        p = int(d[idx + 2])
        m = int(d[idx + 3])
        idx += 4
        a = [int(x) for x in d[idx : idx + n]]
        idx += n

        q = a[:]
        curr_p = p - 1

        def step():
            nonlocal curr_p
            total = 0
            while curr_p >= k:
                low_val = q[0]
                low_idx = 0
                for i in range(1, k):
                    if q[i] < low_val:
                        low_val = q[i]
                        low_idx = i
                total += q.pop(low_idx)
                q.append(low_val)
                if low_idx < curr_p:
                    curr_p -= 1

            v = q.pop(curr_p)
            total += v
            q.append(v)
            curr_p = n - 1
            return total

        c1 = step()
        if c1 > m:
            res.append("0")
        else:
            rem = m - c1
            cl = step()
            res.append(str(1 + rem // cl))

    sys.stdout.write("\n".join(res) + "\n")


if __name__ == "__main__":
    solve()
