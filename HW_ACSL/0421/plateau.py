board = []

for i in range(5):
    board.append([])
    for j in range(5):
        board[i].append(i*5 + j)

# 6, 2B, 7, 4W, 0 1. 0, 4, 2
# 2. 9, 2B, 10, 3W, 0 2. 0, 3, 2
# 3. 8, 3B, 9, 3W, 10, 1W, 0 3. 3, 0, 3
# 4. 13, 4B, 14, 2W, 0 4. 2, 0, 2
# 5. 17, 5B, 18, 2W, 19, 2W, 0 5. 4, 0, 2
# 6. 11, 3B, 16, 4W, 21, 2W, 0 6. 2, 4, 2
# 7. 6, 2B, 16, 2W, 0 7. 2, 0, 2
# 8. 1, 3B, 6, 3W, 11, 2W, 0 8. 3, 0, 3
# 9. 12, 4B, 17, 3W, 0 9. 3, 0, 3
# 10. 9, 4B, 14, 3W, 19, 2W, 24, 2W, 0 10. 4, 0, 2

input = "19, 4B, 14, 3W, 19, 2W, 24, 2W, 0"
inputs = input.split(", ")
startPos, startStack, startColor = int(inputs[0]), int(inputs[1][0]), inputs[1][1]

def moveStack(movesLeft, currPos, stackHeight, score, drops, marks):
    captured, pinned = score
    if movesLeft <= 0 or captured >= 6:
        return score + [max(max(drops), stackHeight)]
    for mark in marks:
        [pos, comp, pom] = mark
        
        if(pos == currPos): continue 
        
        num, color = int(comp[0]), comp[1]
        
        if((getRow(currPos) == getRow(pos) or getCol(currPos) == getCol(pos))and dist(currPos, pos) <= movesLeft):
            
            if(color == "B"):
                movesLeft -= dist(currPos, pos)
                for i in range(1, num):
                    if stackHeight - i >= 0:
                        removeDrop = False
                        if(i not in drops):
                            drops.add(i)
                            removeDrop = True
                        addStack = moveStack(movesLeft, pos, stackHeight - i, [captured, pinned], drops, marks)
                        if(removeDrop): drops.remove(i)
                    minusStack = moveStack(movesLeft, pos, stackHeight + i, [captured, pinned], drops, marks)
                    score = max(addStack, minusStack, score)
            
            if(color == "W" and not pom):
                movesLeft -= dist(currPos, pos)
                if stackHeight >= num:
                    mark[2] = True
                    
                    drops.add(num)
                    capStack = moveStack(movesLeft, pos, stackHeight - num, [captured + num, pinned], drops, marks)
                    score = max(score, capStack)
                    print(drops)
                    drops.remove(num)

                for i in range(stackHeight - 1):
                    mark[2] = True
                    removeDrop = False
                    if(i not in drops):
                        removeDrop = True
                        drops.add(i)
                    pinStack = moveStack(movesLeft, pos, stackHeight - i, [captured, pinned + i], drops, marks)
                    score = max(score, pinStack)
                    if(removeDrop): drops.remove(i)
    
    

    maxHeight = max(max(drops), stackHeight)
    
    if len(score) == 2:
        return score + [maxHeight]

    return score

def getRow(pos):
    return (pos-1) // 5

def getCol(pos):
    return (pos-1) % 5

def dist(pos1, pos2):
    if getRow(pos1) == getRow(pos2):
        return abs(getCol(pos1) - getCol(pos2))
    elif getCol(pos1) == getCol(pos2):
        return abs(getRow(pos1) - getRow(pos2))
    return None

score = [0, 0, startStack]

for i in range(0, startStack):
    maxStack = max(i, startStack - i)
    drops = set([i])
    marks = []
    for j in range(2, len(inputs)-2, 2):
        marks.append([int(inputs[j]), inputs[j + 1], False])
    score = max(moveStack(startStack, startPos, startStack - i, [0, 0], drops, marks), score)

print(score)