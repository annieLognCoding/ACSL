import copy

colors = ["B", "R", "G", "Y", "O", "P"]
cube = dict()

input = "B2 CC1 RC4 CR3"
inputs = input.split(" ")
focus, moves = [inputs[0], inputs[1:]]

def makeCube(cube, input_color, pos):
    for i in range(6):
        cube[i] = []
        color = colors[i]
        if color == input_color: 
            initial_pos = (i, (pos // 3, pos % 3))
        for j in range(3): 
            cube[i].append([f"{color}{j*3}", f"{color}{j*3+1}", f"{color}{j*3+2}"])
    return initial_pos

initial_pos = makeCube(cube, focus[0], int(focus[1]))
print(initial_pos)

def rotate(move, curr_pos):
    face, (xpos, ypos) = curr_pos
    direction, rep = move[:2], int(move[2])
    if(direction[0] == "R"):
        curr_row = xpos // 3
        if(face < 4):
            rotateFaces = [0, 1, 2, 3]
        elif(face == 4):
            rotateFaces = [4, 1, 5, 2]
        else:
            rotateFaces = [5, 2, 4, 1]
        curr_pos = rotateRow(curr_pos, curr_row, rotateFaces, direction, rep)
    return curr_pos

def rotateRow(curr_pos, curr_row, rotateFaces, direction, rep):
    result = None
    cube_copy = copy.deepcopy(cube)
    for i in rotateFaces:
        for j in range(3):
            # print("here", i, j, curr_row, rep + j)
            if direction == "RR":
                if(j - rep <= (curr_row + 1) * 3):
                    shift = (j - rep) // 3
                    new_face = (i - shift) % 4
                    new_pos = (j - rep) % 3
                else:
                    new_face = i
                    new_pos = j - rep
            else:
                if(j + rep >= (curr_row + 1) * 3):
                    shift = (j + rep) // 3
                    new_face = (i + shift) % 4
                    new_pos = (j + rep) % 3
                else:
                    new_face = i
                    new_pos = j + rep
            print(i, new_face, curr_row, new_pos)
            if(curr_pos[0] == new_face and curr_pos[1][1] == new_pos):
                print("hi")
                result = (i, (curr_row, j))
            cube[i][curr_row][j] = cube_copy[new_face][curr_row][new_pos]
        print()
    return result

print(rotate("RC2", initial_pos))
print(cube)









"""
0: RC --> 3 (2), RR --> 1 (0), CC --> 4 (0), CR --> 5 (6)
1: RC --> 0 (2), RR --> 2 (0), CC --> 4 (6), CR --> 5 (0)
2: RC --> 1 (2), RR --> 3 (0), CC --> 4 (8), CR --> 5 (5)
3: RC --> 2 (2), RR --> 0 (0), CC --> 4 (5), CR --> 5 (2)
4: RC --> 0 (0), RR --> 1 (2), CC --> 5 (6), CR --> 1 (0)
5: RC --> 1 (8), RR --> 2 (6), CC --> 1 (6), CR --> 4 (0)
"""