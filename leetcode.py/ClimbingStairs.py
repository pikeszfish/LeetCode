class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        while n > 1:
            a, b = b, (a+b)
            n -= 1
        return a
a = Solution()
print a.climbStairs(35)
