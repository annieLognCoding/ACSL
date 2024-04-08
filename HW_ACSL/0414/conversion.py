import os

elems = ["A", "B", "C", "D", "E"]
table = dict()

def initializeTable():
    for row in elems:
        table[row] = {col: 1 if col == row else 0 for col in elems}

def insertConversion(str):
    splitArray = str.split(",")
    if len(splitArray) != 2: return
    edge, value = splitArray
    first = edge[0]
    second = edge[1]
    table[first][second] = float(value)

def printTable():
    for row in table:
        print(f"{row}: ", end = " ")
        for col in table[row]:
            print(table[row][col], end = " ")
        print()

def convert(first, second):
    visited = set()

    def traverse(node, ratio):
        if(node == second): return 1
        #use visited set to prevent cycles (e.g. A -> B -> A)
        visited.add(node)
        values = table[node]

        #traverse all columns in the row of the "node"
        for elem in values:
            factor = values[elem]
            #if we have a conversion factor, traverse possible paths from here
            #factor * NODE = ELEM 
            if factor != 0 and elem not in visited:
                #if we ended up at our dest, stop and return ratio
                if elem == second:
                    return ratio * factor
                rowTraverse = traverse(elem, ratio * factor)
                if(rowTraverse > 0): return rowTraverse
        
        #traverse all elements of the table
        for elem in table:
            row = table[elem]
            factor = row[node]
            #if we have a conversion factor for the node, traverse possible paths from there
            #factor * ELEM = NODE 
            if factor != 0 and elem not in visited:  
                if elem == second:
                    #if we ended up at our dest, stop and return ratio
                    return ratio * 1/factor
                colTraverse = traverse(elem, ratio * 1/factor)
                if(colTraverse > 0): return colTraverse
        
        return 0 
    
    print('{0:.2f}'.format(traverse(first, 1)))


def main():
    initializeTable()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file1 = open(f'{__location__}/input.txt', 'r')
    lines = file1.readlines()
    print(lines)
    for i in range(len(lines)):
        line = lines[i]
        if i < 4:
            insertConversion(line.strip())
        else:
            edge = line.strip()
            convert(edge[0], edge[1])

main()