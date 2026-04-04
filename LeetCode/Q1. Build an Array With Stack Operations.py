class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        m = []
        res = []  # shoul be equal to target
        reStr = []
        maxx = max(target)
        for i in range(n):
            m.append(i + 1)
        for i in range(n):
            if if target in res:
                return reStr
            res.append(m[i])
            reStr.append("Push")
            if m[i] not in target:
                res.remove(m[i])
                reStr.append("Pop")

            # if res[len(res) - 1] != target[i]:
            # print(res[len(res) - 1], target[i - 1])
            # res.pop(len(res) - 1)
            # print(res, target)


result = Solution().buildArray([2, 3, 4], 4)
print(result)


##ЭТО ДОДЕЛАТЬ НАДО БЛЯТЬ НЕ ЗАБУДЬ
