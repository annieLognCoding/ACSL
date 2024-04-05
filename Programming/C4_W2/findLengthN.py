def readInput(L):
    arr = L.split()
    return [arr[0], arr[1:]]

def travel(n, tEdge, path, edges, paths):
    if(n == 0):
        paths.append(path)
        return
    
    for i in range(0, len(edges)):
        edge = edges[i]
        first = edge[0]
        second = edge[1]
        #if we can travel to the edge and no vertex is repeated
        if(tEdge[1] == first and (second not in path)):
            #travel to the edge and explore all other paths
            travel(n-1, edge, path + second, edges, paths)

def findLengthN(input):
    n, edges = readInput(input)
    paths = []
    sum = 0
    
    for i in range(0, len(edges)):
        edge = edges[i]
        if(edge[0] == edge[1]): continue
        #find all simple paths starting with edge[i]
        travel(int(n)-1, edge, edge, edges, paths)
    
    #add all paths
    for p in set(paths):
        sum += int(p)
        
    return sum    

if __name__ == "__main__":
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
     # Strips the newline character
    for line in Lines:
        print(findLengthN(line.strip()))
