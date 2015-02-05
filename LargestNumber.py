class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num.sort(cmp=self.cmpp)
        print num

    def cmpp(self, a, b):
        if len(str(a)) == len(str(b)):
            return int(b) - int(a)
        else:
            return int(str(b)[0]) - int(str(a)[0])
a = Solution()
print a.largestNumber([3, 30, 34, 5, 9])