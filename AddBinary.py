class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return '{0:b}'.format(int(a, 2) + int(b, 2))