class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = []
        n = len(nums)
        s = set(nums)
        print(nums)
        for i in range(1, n + 1):
            if i not in s:
                ans.append(i)
        return ans


# result = Solution().findDisappearedNumbers([1, 1])
# print(result)
