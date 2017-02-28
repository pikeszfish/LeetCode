class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        l = len(s)
        left = 0
        right = l - 1
        s = s.lower()
        while left < right:
            a = s[left]
            while a and left < right:
                if self.isValid(a):
                    break
                else:
                    left += 1
                    a = s[left]
            b = s[right]
            while b and left < right:
                if self.isValid(b):
                    break
                else:
                    right -= 1
                    b = s[right]
            if a == b:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True

    def isValid(self, c):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return True
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        return False
a = Solution()
print a.isPalindrome("race a car")
