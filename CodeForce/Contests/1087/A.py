t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    p = 0
    v = {0}
    for _ in range(n):
        if s[p] == "R":
            p += 1
        else:
            p -= 1
        v.add(p)
    print(len(v))
