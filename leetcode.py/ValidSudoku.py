class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        a = [0,0,0,0,0,0,0,0,0]
        for i in range(0, 10):
            for i in range(0, 10):
                if board[i][j] != '.':
                    if a[board[i][j]] > 0:
                        return False
                    else:
                        a[board[i][j]] = 1
            a = [0,0,0,0,0,0,0,0,0]
        for i in range(0, 10):
            for i in range(0, 10):
                if board[j][i] != '.':
                    if a[board[j][i]] > 0:
                        return False
                    else:
                        a[board[i][j]] = 1
            a = [0,0,0,0,0,0,0,0,0]
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                
