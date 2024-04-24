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
    if(pathWay == "d"): weight = 1.4
    elif(pathWay == "n"): weight = 1
    else: weight = 0

    if(start == end or count == 4):
        return weight
    
    (sX, sY), (eX, eY) = start, end

    print(f"{start}: {nextDiag(start, end)}")
    nWeight, dWeight, next = None, None, None

    if(sX > eX) and sY % 2 == 0:
        next = (sX - 1, sY)
    if(sX < eX) and sY % 2 == 1:
        next = (sX + 1, sY)
    if(sY > eY) and sX % 2 == 0:
        next = (sX, sY - 1)
    if(sY < eY) and sY % 2 == 1:
        next = (sX, sY + 1)

    if(next):
        nWeight = calcWeight(next, "n", end, count + 1)
    else:
        if sX % 2 == 0:
            nextX = (sX - 1, sY)
        else:
            nextX = (sX + 1, sY)
        if sY % 2 == 0:
            nextY = (sX, sY - 1)
        else:
            nextY = (sX, sY + 1)
        nWeight = min(calcWeight(nextX, "n", end, count + 1), calcWeight(nextY, "n", end, count + 1))


    
    diag = nextDiag(start, end)
    if(diag):
        dWeight = calcWeight(diag, "d", end, count + 1)
    if(nWeight and dWeight):
        pWeight = min(nWeight, dWeight)
    elif (nWeight):
        pWeight = nWeight
    elif (dWeight):
        pWeight = dWeight
    
    return weight + pWeight
    

print(calcWeight((2,1), "s", (2, 2), 0))






