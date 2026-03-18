class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        m = []
        print(len(nums))
        print(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums) - 1:
                    m.append(count)
            else:
                m.append(count)
                count = 0
        return max(m)


# result = Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
# print(result)
