import sys


def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def get_div(n, k):
    return divmod(n, k)[0]


def get_lcm(x, y):
    return get_div(x * y, get_gcd(x, y))


data = sys.stdin.read().split()
if data:
    t = int(data[0])
    p = 1
    for _ in range(t):
        a = int(data[p])
        b = int(data[p + 1])
        c = int(data[p + 2])
        m = int(data[p + 3])
        p += 4

        ab = get_lcm(a, b)
        ac = get_lcm(a, c)
        bc = get_lcm(b, c)
        abc = get_lcm(ab, c)

        na = get_div(m, a)
        nb = get_div(m, b)
        nc = get_div(m, c)
        nab = get_div(m, ab)
        nac = get_div(m, ac)
        nbc = get_div(m, bc)
        nabc = get_div(m, abc)

        res_a = 6 * na - 3 * nab - 3 * nac + 2 * nabc
        res_b = 6 * nb - 3 * nab - 3 * nbc + 2 * nabc
        res_c = 6 * nc - 3 * nac - 3 * nbc + 2 * nabc

        print(res_a, res_b, res_c)
