def solve():
    s, n = map(int, input().split())
    weights = list(map(int, input().split()))
    dp = [0] * (s + 1)
    dp[0] = 1
    # print(s, n)
    # print(weights)

    for weight in weights:
        for i in range(s, weight - 1, -1):
            if dp[i - weight]:
                dp[i] = 1

    otvet = []
    for i in range(s + 1):
        if dp[i]:
            otvet.append(i)
    print(max(otvet))


if __name__ == "__main__":
    solve()
