class Solution(object):
    def __init__(self):
        self.result = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = set()
        self.solveNQueensRecur(board, 0, n)
        return self.result
       
    
    def solveNQueensRecur(self, board, i, n):
        if(i == n):
            if(len(board) == n):
                self.result.append(sorted(list(board)))
            board = set()
            return

        for j in range(n):
            if(not (diagExists(board, i, j) or rowExists(board, i, j) or colExists(board, i, j))):
                board.add((i, j))
                self.solveNQueensRecur(board, i+1, n)
                board.remove((i, j))
                        
def diagExists(board, i, j):
        for pos in board:
            (row, col) = pos
            if abs(row - i) == abs(col - j):
                return True
        return False
    
def rowExists(board, i, j):
    for pos in board:
        (row, col) = pos
        if i == row:
            return True
    return False

def colExists(board, i, j):
    for pos in board:
        (row, col) = pos
        if j == col:
            return True
    return False

s = Solution()
print(len(s.solveNQueens(9)))