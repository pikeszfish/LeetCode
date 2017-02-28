class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0
        lens = 0
        for i in xrange(0, len(A)):
            p = A.pop(0)
            if p != elem:
                A.append(p)
                lens += 1
        return lens