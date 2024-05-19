grid = []
groups = []
def readInput(line):
    global grid

    inputs = line.split(",")
    r, c = int(inputs[0]), int(inputs[1])
    for i in range(r):
        grid.append([0] * c)    
    config = inputs[2].strip()
    n = int(inputs[3])
    for i in range(1, n+1):
        pos_val = inputs[3 + i].strip()
        row = r - int(pos_val[0])
        col = int(pos_val[1]) - 1
        val = int(pos_val[2])
        grid[row][col] = val
    return config
        

def reorder(config):    
    i, j = len(grid) - 1, len(grid[0])
    ind = (i) * j
    col_count = 0
    rows = []
    line = ""
    while ind >= 0:
        line += config[ind]
        ind += 1
        col_count += 1
        if(col_count == j):
            i -= 1
            ind = (i) * j
            col_count = 0
            rows.append(line)
            line = ""
    return rows

def hexToBin(hex_char):
    # Create a dictionary to map hex characters to their binary equivalents
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    # Convert the hex character to uppercase to handle lowercase input
    hex_char = hex_char.upper()
    
    # Return the binary equivalent from the dictionary
    return hex_to_bin.get(hex_char, 'Invalid hex character')


def makeGroup(tile, back, currPos, rows, group, filled):
    global groups
    
    border = hexToBin(tile)
    avail = {}
    avail["top"], avail["right"], avail["bottom"], avail["left"] = 1 - int(border[0]), 1 - int(border[1]), 1 - int(border[2]), 1 - int(border[3])
    
    print(currPos, tile, back, avail)

    if(back in avail and not avail[back]):
        return group
    elif back in avail:
        group.append(currPos)
        filled[currPos] = 1
        avail[back] = 0

    if avail["top"] and currPos[0] > 0:
        nextPos = (currPos[0] - 1, currPos[1])
        tile = rows[nextPos[0]][nextPos[1]]
        if(nextPos not in group):
            makeGroup(tile, "bottom", nextPos, rows, group, filled)
    if avail["right"] and currPos[1] < len(grid[0]) - 1:
        nextPos = (currPos[0], currPos[1] + 1)
        tile = rows[nextPos[0]][nextPos[1]]
        if(nextPos not in group):
            makeGroup(tile, "left", nextPos, rows, group, filled)
    if avail["bottom"] and currPos[0] < len(grid) - 1:
        nextPos = (currPos[0] + 1, currPos[1])
        tile = rows[nextPos[0]][nextPos[1]]
        if(nextPos not in group):
            makeGroup(tile, "top", nextPos, rows, group, filled)
    if avail["left"] and currPos[1] > 0:
        nextPos = (currPos[0], currPos[1] - 1)
        tile = rows[nextPos[0]][nextPos[1]]
        if(nextPos not in group):
            makeGroup(tile, "right", nextPos, rows, group, filled)

    return group

def makeGroups(rows):
    r, c = len(grid), len(grid[0])
    filled = {}
    for i in range(r):
        for j in range(c):
            filled[(i, j)] = 0
    
    print(filled)
    for i in range(r):
        for j in range(c):
            if not filled[(i, j)]:
                group = [(i, j)]
                tile = rows[i][j]
                groups.append(makeGroup(tile, "", (i, j), rows, group, filled))    



config = readInput('3, 5, 32EB69CB6DFBE9E, 2, 114, 151')
print(grid)
rows = reorder(config)
print(rows)
makeGroups(rows)
print(groups)