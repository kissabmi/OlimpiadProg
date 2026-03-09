class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        T0 = 0
        T1 = 1
        T2 = 1

        while n > 2:
            t2 = T2
            t1 = T1
            T2 = T2 + T1 + T0
            T1 = t2
            T0 = t1
            n -= 1

        return T2


# if __name__ == "__main__":
#     print(Solution().tribonacci(25))

# рекурсия время руинит
