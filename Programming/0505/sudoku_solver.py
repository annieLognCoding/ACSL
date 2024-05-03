class Solution(object):
    def __init__(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.cols = [[] for i in range(len(board))]
        self.squares = [[] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == '.'): elem = 0
                else: elem = int(board[i][j])
                self.cols[j].append(elem)
                print(i, j, (i//3 * 3+ j//3))
                self.squares[(i//3 * 3 + j//3)].append(elem)

    def solveSudoku(self, i, j, elem):
        temp_row = self.board[i][j]
        temp_col = self.cols[j][i]
        temp_square = self.squares[(i//3)*3 + j//3][j]
        self.board[i][j] = elem
        self.cols[j][i] = elem
        self.squares[(i//3 * 3 + j//3)] = elem
        if(i == 8 and j == 8): return

    def rowOkay(self):
        for row in (self.board):
            if(row): return False


    

sol = Solution([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
sol.solveSudoku()
