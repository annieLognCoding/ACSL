diagonalSeeds = [{"start": (5,2), "end": (1,6)}, {"start": (1,2), "end": (3,4)}, {"start": (2,2), "end": (5,5)}]

diagonals = []

for seed in diagonalSeeds:
    diagonal = []
    start = seed["start"]
    end = seed["end"]
    (sX, sY), (eX, eY) = start, end
    x, y = sX, sY
    diagonal.append((x,y))
    for i in range(abs(eY - sY)):
        if sX > eX:
            x -= 1
        else:
            x += 1
        y += 1
        diagonal.append((x, y))
    diagonals.append(diagonal)


def diagPath(start, end):
    for diag in diagonals:
        for ind in range(len(diag) - 1):
            path = [diag[ind], diag[ind + 1]]
            if [start, end] == path or [start, end] == path[::-1]:
                return True
    return False


def nextDiag(start, mid):
    (sX, sY), (mX, mY) = start, mid
    dX, dY = (sX, sY)
    
    if(sX < mX):
        dX += 1
    elif(sX > mX):
        dX -= 1
    
    if(sY < mY):
        dY += 1
    elif(sY > mY):
        dY -= 1
    
    diag = (dX, dY)

    if diagPath(start, diag):
        return diag
    else:
        return False


def calcWeight(start, pathWay, end, count):
    if(not start or count < 0): return False
    if(pathWay == "d"): weight = 1.4
    elif(pathWay == "n"): weight = 1
    else: weight = 0

    if(start == end):
        return weight
    
    (sX, sY) = start
    
    nWeight, dWeight = None, None
    nextX, nextY = None, None

    # optimize?
    if sY % 2 == 0 and sX > 1:
        nextX = (sX - 1, sY)
    elif sY % 2 == 1 and sX < 6:
        nextX = (sX + 1, sY)
    if sX % 2 == 0 and sY > 1:
        nextY = (sX, sY - 1)
    elif sX % 2 == 1 and sY < 6:
        nextY = (sX, sY + 1)
    
    xWeight = calcWeight(nextX, "n", end, count-1)
    yWeight = calcWeight(nextY, "n", end, count-1)
    
    if(xWeight and yWeight):
        nWeight = min(xWeight, yWeight)
    elif(xWeight):
        nWeight = xWeight
    else:
        nWeight = yWeight
    
    diag = nextDiag(start, end)

    pWeight = None
    dWeight = calcWeight(diag, "d", end, count-1)

    if(nWeight and dWeight):
        pWeight = min(nWeight, dWeight)
    elif (nWeight):
        pWeight = nWeight
    elif (dWeight):
        pWeight = dWeight
    else:
        return False
        
    return weight + pWeight
    
start, end = (2, 5), (6, 3)
count = abs(start[0] - end[0]) + abs(start[1] - end[1]) + 6
print(calcWeight(start, "s", end, count))
"""
1. 1,1,2,1 1. 1
 2. 1,1,1,2 2. 1
 3. 2,1,2,2 3. 3
 4. 2,1,1,2 4. 4
 5. 4,1,2,2 5. 5
 6. 1,2,2,3 6. 1.4
 7. 2,2,5,5 7. 4.2
 8. 1,2,4,3 8. 3.4
 9. 5,5,4,3 9. 2.4
 10. 2,5,6,3 10. 4.8
"""





