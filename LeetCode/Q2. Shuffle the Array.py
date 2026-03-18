class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans


result = Solution().shuffle([2, 5, 1, 3, 4, 7], 3)
print(result)
