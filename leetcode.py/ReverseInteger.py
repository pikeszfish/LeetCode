class Solution:
    # @return an integer
    def reverse(self, x):
        flag = False
        if x < 0:
            flag = True
        y = str(x).strip('-')[::-1]
        if flag:
            return int('-'+y) if int('-'+y) > -2147483648 else 0
        else:
            return int(y) if int(y) < 2147483649 else 0
