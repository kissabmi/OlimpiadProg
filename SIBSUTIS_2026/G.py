import sys

# def solve():
#     data = sys.stdin.readline().split()
#     n = int(data[0])
#     m = int(data[1])
#     # print("test", n, m)
#     intLogs = [0] * m
#     strLogs = [""] * m
#     currentanswer = [0] * n
#     answer = [0] * n
#     for i in range(m):
#         data = sys.stdin.readline().split()
#         intLogs[i] = int(data[0])
#         strLogs[i] = data[1]
#         # print("лог", intLogs[i], strLogs[i])

#     for j in range(n):
#         for i in range(m):
#             if intLogs[i] == j + 1 and strLogs[i] == "+":
#                 currentanswer[j] += 1
#                 if currentanswer[j] > answer[j]:
#                     answer[j] = currentanswer[j]
#             elif intLogs[i] == j + 1 and strLogs[i] == "-":
#                 currentanswer[j] -= 1

#     for i in range(n):
#         # if i == n:
#         #     print(answer[i])
#         # else: ппц там ряльно есть пробел , а вот в шк 21 не было бы там пробела и всо гг
#         print(answer[i], end=" ")


def solve():
    data = sys.stdin.readline().split()
    n = int(data[0])
    m = int(data[1])

    current = [0] * (n + 1)
    answer = [0] * (n + 1)

    for i in range(m):
        data = sys.stdin.readline().split()
        category = int(data[0])
        action = data[1]

        if action == "+":
            current[category] += 1
            if current[category] > answer[category]:
                answer[category] = current[category]
        else:
            current[category] -= 1

    for i in range(1, n + 1):
        print(answer[i])


if __name__ == "__main__":
    solve()
