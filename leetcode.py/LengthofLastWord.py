class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip().split(' ')[-1].strip(',')
        return len(s)
a = Solution()
print a.lengthOfLastWord("Hello World")