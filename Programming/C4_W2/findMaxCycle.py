def readInput(L):
    arr = L.split()
    tuples = []
    for i in range(0, len(arr), 2):
        tuples.append((arr[i], int(arr[i + 1])))
    return tuples

def travel(start, tEdge, path, edges, tWeight, maxVal):
    #look at all the edges and see if they are traversable
    for i in range(0, len(edges)):
        edge = edges[i][0]
        weight = edges[i][1]
        #see if we can travel by the edge
        if(tEdge[1] == edge[0]):
            #see if the edge creates a cycle
            if(edge[1] == start):
                #store maxValue if cycle weight is bigger
                maxVal = max(tWeight + weight, maxVal) if maxVal else (tWeight + weight)
            if (edge[1] not in path):
                #if the second vertex is not repeated,
                #either travel the edge, or continue to iterate the rest of the graph without the edge
                maxVal = travel(start, edge, path + edge[1], edges, tWeight + weight, maxVal)
                
    return maxVal if maxVal else False

def findMaxCycle(input):
    edges = readInput(input)
    values = []
    
    for i in range(0, len(edges)):
        edge = edges[i][0]
        weight = edges[i][1]
        first = edge[0]
        second = edge[1]
        #add any loops
        if(first == second):
            values.append(weight)
            continue
        #travel from each edge
        values.append(travel(first, edge, edge, edges, weight, False))
        
    maxVal = values[0]
    #find max-valued cycle
    for x in values:
        if(x == False):
            continue
        if(x > maxVal):
            maxVal = x
    return maxVal if maxVal else 0

if __name__ == "__main__":

    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
     # Strips the newline character
    for line in Lines:
        print(findMaxCycle(line.strip()))
