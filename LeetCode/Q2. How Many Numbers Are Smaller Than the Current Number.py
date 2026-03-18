class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
                if j == len(nums) - 1:
                    ans.append(count)
        return ans


# result = Solution().smallerNumbersThanCurrent([6, 5, 4, 8])
# print(result)
# решение ща оч не оптимальное хотя по памяти вроде норм
