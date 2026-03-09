class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        list = [0, 0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    list[0] = i
                    list[1] = j
        return list

    def sort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums


# result = Solution().sort(Solution().twoSum([3, 3], 6))
# print(result)
