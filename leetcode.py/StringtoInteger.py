class Solution:
    # @return an integer
    def atoi(self, str):
        if not str:
            return 0
        str = str.strip()
        flag = False
        if str[0] == '-':
            flag = True
            str = str[1:]
        if str[0] == '+':
            if flag:
                return 0
            str = str[1:]
        result = 0
        for i in str:
            if ord(i) >= ord('0') and ord(i) <= ord('9'):
                result = result * 10 + int(i)
            else:
                break
        result = -1*result if flag else result
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        return result
a = Solution()
print a.atoi("-2147483649")