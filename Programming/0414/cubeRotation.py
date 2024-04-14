import copy

colors = ["B", "R", "G", "Y", "O", "P"]
cube = dict()

## Processing input
input = "G1 CC1 RR5 CR7 RC3"
inputs = input.split(" ")

### store focus tile and all the moves
focus, moves = [inputs[0], inputs[1:]]

##Make Cube and store initial position
def makeCube(cube, input_color, pos):
    for i in range(6):
        cube[i] = []
        color = colors[i]
        if color == input_color: 
            #if the focus tile is this color, store this face as the starting point 
            initial_pos = (i, (pos // 3, pos % 3))
        for j in range(3): 
            cube[i].append([f"{color}{j*3}", f"{color}{j*3+1}", f"{color}{j*3+2}"])
    return initial_pos

initial_pos = makeCube(cube, focus[0], int(focus[1]))
print(cube)
def rotate(move, curr_pos):
    face, (curr_row, curr_col) = curr_pos
    major, direction, rep = move[0], move[1], int(move[2])
    rotateArray = []
    
    ##Store all positions of Rotate Groups
    if(major == "R"):
        if(face <= 3):
            rotateArray =[
                (0, (curr_row, 0)), (0, (curr_row, 1)), (0, (curr_row, 2)),    
                (1, (curr_row, 0)), (1, (curr_row, 1)), (1, (curr_row, 2)),    
                (2, (curr_row, 0)), (2, (curr_row, 1)), (2, (curr_row, 2)),    
                (3, (curr_row, 0)), (3, (curr_row, 1)), (3, (curr_row, 2)) 
            ]
            
        if(face == 4):
            rotateArray = [
                (4, (curr_row, 0)), (4, (curr_row, 1)), (4, (curr_row, 2)),
                (2, (0, 2-curr_row)), (2, (1, 2-curr_row)), (2, (2, 2-curr_row)),
                (5, (2-curr_row, 2)), (5, (2-curr_row, 1)), (5, (2-curr_row, 0)),
                (0, (2, curr_row)), (0, (1, curr_row)), (0, (0, curr_row))
             ]
        if(face == 5):
            rotateArray = [
                (5, (curr_row, 0)), (5, (curr_row, 1)), (5, (curr_row, 2)),
                (2, (2, curr_row)), (2, (1, curr_row)), (2, (0, curr_row)),
                (4, (2-curr_row, 2)), (4, (2-curr_row, 1)), (4, (2-curr_row, 0)),
                (0, (0, 2-curr_row)), (0, (1, 2-curr_row)), (0, (2, 2-curr_row))
            ]
        
    if(major == "C"):
        if face in [1, 5, 3, 4]:
            rotateArray = [
                (1, (0, curr_col)),  (1, (1, curr_col)), (1, (2, curr_col)),
                (5, (0, curr_col)),  (5, (1, curr_col)), (5, (2, curr_col)),
                (3, (2, 2-curr_col)), (3, (1, 2-curr_col)), (3, (0, 2-curr_col)),
                (4, (0, curr_col)),  (4, (1, curr_col)), (4, (2, curr_col))
            ]
        if(face == 0):
            rotateArray = [
                (0, (0, curr_col)), (0, (1, curr_col)), (0, (2, curr_col)),
                (5, (2-curr_col, 0)), (5, (2-curr_col, 1)), (5, (2-curr_col, 2)),
                (2, (2, 2-curr_col)), (2, (1, 2-curr_col)), (2, (0, 2-curr_col)),
                (4, (curr_col, 2)), (4, (curr_col, 1)), (4, (curr_col, 0))
             ]
        if(face == 2):
            rotateArray = [
                (2, (0, curr_col)), (2, (1, curr_col)), (2, (2, curr_col)),
                (5, (curr_col, 2)), (5, (curr_col, 1)), (5, (curr_col, 0)),
                (0, (2, 2-curr_col)), (0, (1, 2-curr_col)), (0, (0, 2-curr_col)),
                (4, (2-curr_col, 0)), (4, (2-curr_col, 1)), (4, (2-curr_col, 2))
            ]
    
    result = rotateMajor(rotateArray, direction, rep)
    
    #reassign values to the rotated row or column
    for i in range(len(rotateArray)):
        face, (row, col) = rotateArray[i]
        cube[face][row][col] = result[i]
        if(focus == result[i]):
            curr_pos = (face, (row, col))
    return curr_pos

#rotate the array according to the number of repetitions 
def rotateMajor(rotateArray, direction, rep):
    result = []
    if(direction == "C"):
        for i in range(len(rotateArray)):
            face, (row, col) = rotateArray[(i + rep) % len(rotateArray)]
            result.append(cube[face][row][col])
    else:
       for i in range(len(rotateArray)):
            face, (row, col) = rotateArray[(i - rep) % len(rotateArray)]
            result.append(cube[face][row][col]) 
    return result


# curr_pos = initial_pos

# for move in moves:
#     curr_pos = rotate(move, curr_pos)

# face = curr_pos[0]
# for row in cube[face]:
#     for square in row:
#         print(square, end = "")
