class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        nums = []
        i = 0
        while x > 0:
            nums.append(x % 10)
            x = x // 10
            i += 1
        # print(nums)
        # print(i)
        count = 0
        if i % 2 == 0:
            l = i - 1
            f = 0
            while nums[l] == nums[f] and f <= i / 2 and l >= i / 2:
                count += 1
                l -= 1
                f += 1
            if i / 2 == count:
                return True
        if i % 2 != 0:
            l = i - 1
            f = 0
            while nums[l] == nums[f] and f < (i - 1) / 2 and l > (i - 1) / 2:
                count += 1
                l -= 1
                f += 1
                # print(count,nums[l],nums[f])
            if (i - 1) / 2 == count:
                return True
        return False


# result = Solution().isPalindrome(n)
# print(result)
