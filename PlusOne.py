class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        num = 0
        for i in digits:
            num = num * 10 + int(i)
        num += 1
        return [int(i) for i in str(num)]
a = Solution()
print (a.plusOne([1,2,3,4,5]))