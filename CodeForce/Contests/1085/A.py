t = int(input().strip())

results = []

for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    perm_zero = [False] * n

    if s[0] == "0":
        perm_zero[0] = True
    if s[-1] == "0":
        perm_zero[-1] = True

    for i in range(n - 1):
        if s[i] == "0" and s[i + 1] == "0":
            perm_zero[i] = True
            perm_zero[i + 1] = True

    max_ones = n - sum(perm_zero)

    min_ones = 0
    current_segment_len = 0

    for i in range(n):
        if not perm_zero[i]:
            current_segment_len += 1
        else:
            if current_segment_len > 0:
                min_ones += current_segment_len // 2 + 1
                current_segment_len = 0

    if current_segment_len > 0:
        min_ones += current_segment_len // 2 + 1

    results.append(f"{min_ones} {max_ones}")

print("\n".join(results))
