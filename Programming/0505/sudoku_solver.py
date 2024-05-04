class Solution(object):
    def __init__(self, board):
        self.board = []
        self.cols = [[] for _ in range(9)]
        self.squares = [[] for _ in range(9)]
        self.empty = []

        for i in range(9):
            self.board.append([])
            for j in range(9):
                if board[i][j] == '.':
                    val = 0
                    self.empty.append((i, j))
                else:
                    val = int(board[i][j])
                self.board[i].append(val)
                self.cols[j].append(val)
                self.squares[(i//3 * 3 + j//3)].append(val)

    def insertTile(self, i, j, elem):
        if elem not in self.board[i] and elem not in self.cols[j] and elem not in self.squares[(i // 3)*3 + j//3]:
            return True
        return False

    def solveSudoku(self):
        if not self.empty:
            return True
        
        i, j = self.empty[-1]  
        b = (i // 3) * 3 + (j // 3)
        
        for elem in range(1, 10):
            if self.insertTile(i, j, elem):
                self.board[i][j] = elem
                self.cols[j][i] = elem
                self.squares[b][i%3 * 3 + j%3] = elem  
                self.empty.pop()
                if self.solveSudoku():
                    return True

                # Undo changes if not successful
                self.board[i][j] = 0
                self.cols[j][i] = 0
                self.squares[b][i%3 * 3 + j%3] = 0  
                self.empty.append((i, j)) 
        
        return False

# Example board setup
input_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solver = Solution(input_board)
solver.solveSudoku()
print([[str(num) if num != 0 else '.' for num in row] for row in solver.board])