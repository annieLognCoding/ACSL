dim = -1

def readInput(string):
    global dim
    
    numArr = string.split()
 
    dim = int(numArr[0])
    exc = int(numArr[1])
    moves = numArr[2:]
    
    table = []
    count = 1

    for i in range(dim):
        table.append([])
        for j in range(dim):
            if(count != exc):
                table[i].append(count)
                count += 1
            else:
                exc = -1
                table[i].append(0)
    return (table, moves)

def move(table, moves):
    for move in moves:
        for i in range(len(table)):
            for j in range(len(table[i])):
                if(table[i][j] == int(move)):
                    pos = (i, j)
        (major, ind) = col_or_row(pos, table)
        zeroPos = moveMajor(major, pos, ind, table)
    return zeroPos


def col_or_row(pos, table):
    
    (r, c) = pos

    for j in range(len(table[r])):
        if(table[r][j] == 0):
            return ("row", j)
    for i in range(len(table)):
        if(table[i][c] == 0):
            return ("col", i)

def moveMajor(major, pos, ind, table):
    (r, c) = pos

    if(major == "row"):
        step = 1
        if(ind > c):
            step = -1
        for j in range(ind, c, step):
            table[r][j] = table[r][j + step]
        table[r][c] = 0

    if(major == "col"):
        step = 1
        if(ind > r):
            step = -1
        for i in range(ind, r, step):
            table[i][c] = table[i + step][c]
        table[r][c] = 0

    return r*dim + c + 1

(table, moves) = readInput("5 13 14 19 17 3 8")
print(move(table, moves))
print(table)

