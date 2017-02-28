class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        print A
        print B
        C = A.extend(B)
        print C
        # return A.sort()
a = Solution()
a.merge([1], 1, [11], 0)