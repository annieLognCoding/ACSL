import random
field = []
def move_and_merge_until_stable(row):
    # Remove zeros and prepare for merging
    row = [i for i in row if i != 0]
    can_merge = True

    # Continue merging until no further merges can be done
    while can_merge:
        new_row = []
        skip = False
        can_merge = False  # Reset merge possibility
        for i in range(len(row)):
            if skip:
                skip = False
                continue

            # Check for possible merge
            if i + 1 < len(row) and row[i] == row[i + 1]:
                new_row.append(row[i] * 2)
                skip = True
                can_merge = True  # Continue merging since a merge was made
            else:
                new_row.append(row[i])

        row = new_row

    # Fill the remaining spaces with zeros
    row.extend([0] * (4 - len(row)))  # Assuming a standard 2048 grid size of 4x4
    return row

def move_left(board):
    for idx in range(len(board)):
        board[idx] = move_and_merge_until_stable(board[idx])
    return board

def move_right(board):
    new_board = []
    for row in board:
        reversed_row = list(reversed(row))  # Reverse the row
        merged_row = move_and_merge_until_stable(reversed_row)  # Merge
        new_board.append(list(reversed(merged_row)))  # Reverse back and add to new_board
    return new_board

def move_up(board):
    # Transpose the board
    transposed_board = [list(row) for row in zip(*board)]
    moved_board = move_left(transposed_board)
    # Transpose back to the original orientation
    new_board = [list(row) for row in zip(*moved_board)]
    return new_board

def move_down(board):
    # Transpose the board
    transposed_board = [list(row) for row in zip(*board)]
    moved_board = move_right(transposed_board)
    # Transpose back to the original orientation
    new_board = [list(row) for row in zip(*moved_board)]
    return new_board


def is_game_over(board):
    for i in range(len(board)):
        for j in range(len(board[0]) - 1):
            if board[i][j] == board[i][j + 1] or board[i][j] == 0:
                return False
            if i < len(board) - 1 and board[i][j] == board[i + 1][j]:
                return False
    return True

def get_score(board):
    # Calculate the sum of the tiles
    score = 0
    for row in board:
        for col in row:
            score += col

    return score

def add_new_tile(board):
    ind = []
    for i in range(4):
        if(board[i][0] == 0):
            ind.append((i, 0))
        if(board[i][3] == 0):
            ind.append((i, 3))
        if(board[0][i] == 0):
            ind.append((0, i))
        if(board[3][i] == 0):
            ind.append((3, i))
    randInd = int(random.random() * len(ind))
    (row, col) = ind[randInd]
    board[row][col] = 2
    return board

def recursive_search(board, depth, max_depth):
    global field
    if depth == max_depth or is_game_over(board):
        return get_score(board)
    
    best_score = 0
    moves = [move_left, move_right, move_up, move_down]
    
    for move in moves:
        new_board = move(board.copy())  # Always work on a copy of the board
        if new_board != board:
            new_board = add_new_tile(new_board)
            score = recursive_search(new_board, depth + 1, max_depth)
            if score > best_score:
                best_score = score
                field = new_board
    
    return best_score

# To call the function:
max_depth = 10
initial_board = [[2,4,4,8], [2,2,4,8], [0,0,0,2], [2,2,4,8]]  # Your starting configuration
print(recursive_search(initial_board, 0, max_depth))
print(field)
# optimal_score = recursive_search(initial_board, 0, max_depth)