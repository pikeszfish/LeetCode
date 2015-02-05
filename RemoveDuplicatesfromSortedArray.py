class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        a_len = len(A)
        l = 0
        s = None
        for i in range(0, a_len):
            e = A[i]
            if s != e:
                s = e
                A[l] = s
                l += 1
        A = A[a_len:]
        return l