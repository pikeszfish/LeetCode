class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        t = '1'
        while n > 1:
            result = ''
            n -= 1
            s = t[0]
            k = 1
            for i in range(1, len(t)):
                if t[i] == s:
                    k += 1
                else:
                    result = result + str(k) + str(s)
                    s = t[i]
                    k = 1
            result += str(k) + str(s)
            t = result
        return result
b = Solution()
print b.countAndSay(5)