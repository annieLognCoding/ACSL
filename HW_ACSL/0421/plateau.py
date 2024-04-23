import os

#try out all possible moves
def moveStack(major, movesLeft, currPos, stackHeight, score, marks):
    captured, pinned, maxHeight = score
    
    #if we are out of moves or markers or we won, end the game
    if movesLeft <= 0 or captured >= 6 or stackHeight == 0:
        #max height will either be the maximum dropped stack height
            #or the current stack height
        maxHeight = max(maxHeight, stackHeight)
        return [captured, pinned, maxHeight] 
    
    #for every position with other markers
    for mark in marks:
        [pos, comp, pom] = mark
        
        #skip current position
        if(pos == currPos): continue 
        num, color = int(comp[0]), comp[1]
        distance = dist(currPos, pos)
        
        #if the position is reachable, try it
            #But only if the move aligns with the current major
        if((major == "R" and getRow(currPos) == getRow(pos) or major == "C" and getCol(currPos) == getCol(pos))and distance <= movesLeft):
            
            #if we land on our team marker,
                #try dropping / adding markers to the current stack
                #when we drop markers, save it as a possible max stack height
            if(color == "B"):
                for i in range(1, num):
                    if stackHeight - i >= 0:
                        minusStack = moveStack(major, movesLeft - distance, pos, stackHeight - i, [captured, pinned, max(i, maxHeight)], marks)
                    addStack = moveStack(major, movesLeft - distance, pos, stackHeight + i, [captured, pinned, maxHeight], marks)
                    score = max(addStack, minusStack, score)
            
            #if we land on opponent markers that are not already captured or pinned,
                #try capturing them or pinning them
            if(color == "W" and not pom):
                if stackHeight >= num:
                    
                    #for this recursive call, we will no longer come back to this stack
                    mark[2] = True
                    capStack = moveStack(major, movesLeft - distance, pos, stackHeight - num, [captured + num, pinned, max(maxHeight, num)], marks)
                    score = max(score, capStack)
                    mark[2] = False
                
                for i in range(1, stackHeight + 1):
                    #for this recursive call, we will no longer come back to this stack
                    mark[2] = True                      
                    pinStack = moveStack(major, movesLeft - distance, pos, stackHeight - i, [captured, pinned + num, max(i, maxHeight)], marks)
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
    
    #build the board for the input
    marks = []        
    for j in range(2, len(inputs)-2, 2):
        marks.append([int(inputs[j]), inputs[j + 1], False])
    
    #try every possible initial stack height
    for i in range(0, startStack + 1):
        score = max(moveStack("R", startStack, startPos, startStack - i, [0, 0, i], marks), score)
        score = max(moveStack("C", startStack, startPos, startStack - i, [0, 0, i], marks), score)

    print(score)