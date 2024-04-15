import os

def moveStack(movesLeft, currPos, stackHeight, score, marks):
    captured, pinned, maxHeight = score
    
    if movesLeft <= 0 or captured >= 6 or stackHeight == 0:
        maxHeight = max(maxHeight, stackHeight)
        return [captured, pinned, maxHeight] 
    
    for mark in marks:
        [pos, comp, pom] = mark
        
        if(pos == currPos): continue 
        num, color = int(comp[0]), comp[1]
        distance = dist(currPos, pos)
        
        if((getRow(currPos) == getRow(pos) or getCol(currPos) == getCol(pos))and distance <= movesLeft):
            if(color == "B"):
                for i in range(1, num):
                    if stackHeight - i >= 0:
                        minusStack = moveStack(movesLeft - distance, pos, stackHeight - i, [captured, pinned, max(i, maxHeight)], marks)
                    addStack = moveStack(movesLeft - distance, pos, stackHeight + i, [captured, pinned, maxHeight], marks)
                    score = max(addStack, minusStack, score)
            
            if(color == "W" and not pom):
                if stackHeight >= num:
                    mark[2] = True
                    capStack = moveStack(movesLeft - distance, pos, stackHeight - num, [captured + num, pinned, max(maxHeight, num)], marks)
                    score = max(score, capStack)
                    mark[2] = False
                
                for i in range(1, stackHeight + 1):
                    mark[2] = True                      
                    pinStack = moveStack(movesLeft - distance, pos, stackHeight - i, [captured, pinned + num, max(i, maxHeight)], marks)
                    score = max(score, pinStack)
                    mark[2] = False
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


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(f'{__location__}/input.txt', 'r')
lines = file1.readlines()

for line in lines:
    inputs = line.split(", ")
    startPos, startStack, startColor = int(inputs[0]), int(inputs[1][0]), inputs[1][1]
    score = [0, 0, 0]
    for i in range(0, startStack + 1):
        marks = []
        for j in range(2, len(inputs)-2, 2):
            marks.append([int(inputs[j]), inputs[j + 1], False])
        score = max(moveStack(startStack, startPos, startStack - i, [0, 0, i], marks), score)
    print(score)