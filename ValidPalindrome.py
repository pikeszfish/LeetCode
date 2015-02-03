class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        i = 0
        j = -1
        while i < j:
            while 