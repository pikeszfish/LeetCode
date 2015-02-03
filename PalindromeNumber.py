class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        k = -1
        for i in str(x):
            if i != str(x)[k]:
                return False
            k -= 1
        return True
a = Solution()
print a.isPalindrome(12321)