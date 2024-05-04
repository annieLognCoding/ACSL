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

    def insertTile(self, i, j, elem):
        if(not(elem in self.board[i] and elem in self.cols[j] and elem in self.squares[(i // 3)*3 +j//3])):
            self.board[i][j] = elem
            self.cols[j][i] = elem
            self.squares[(i//3 * 3 + j//3)] = elem
            return True
        else:
            return False

    def solveSudoku(self):
        pass


    

sol = Solution([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
sol.solveSudoku()
