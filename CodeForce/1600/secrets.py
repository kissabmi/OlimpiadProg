import sys

# import time


def solve():
    n = int(sys.stdin.readline())

    # digits = []
    # temp_n = n
    # while temp_n > 0:
    #     digits.append(temp_n % 3)
    #     print(temp_n)
    #     print(digits)
    #     temp_n //= 3

    # print(sum(digits))

    # temp_n = n
    # count = 0
    # i = 30
    # while temp_n > 0:
    #     # time.sleep(1)
    #     # print(i)
    #     # print(temp_n)
    #     # print(3**i)

    #     if temp_n >= 3**i:
    #         temp_n -= 3**i
    #         count += 1
    #     else:
    #         i -= 1

    # print(count)

    # n = int(input())

    power = 1
    while power <= n:
        if n % power != 0:
            break
        power *= 3

    ans = n // power + 1
    print(ans)


solve()
