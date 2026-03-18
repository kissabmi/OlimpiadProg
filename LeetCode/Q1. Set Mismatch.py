class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        ans = []
        nums.sort()
        # print(nums)
        contains = [0] * len(nums)
        count = 0

        for i in range(len(nums)):
            if not nums.__contains__(i + 1):
                ans.insert(1, i + 1)

        for i in range(len(nums)):
            if nums.__contains__(i + 1):
                nums.remove(i + 1)
        ans.insert(0, nums[0])
        return ans


result = Solution().findErrorNums([1, 1])
print(result)
