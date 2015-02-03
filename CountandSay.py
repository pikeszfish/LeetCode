class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        # a = []
        while n > 1:
            a = []
            for i in xrange(0, 10):
                a.append(0)
            for i in s:
                a[int(i)] += 1
            t = ''
            for i in xrange(9, -1, -1):
                if a[i] > 0:
                    t += str(a[i]) + str(i)
            s = t
            n -= 1
        return t
b = Solution()
print b.countAndSay(4)