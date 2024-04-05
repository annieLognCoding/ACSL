from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)
 
    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)
    
    def dfs(self):
        if(not self.adjList): return
        root = next(iter(self.adjList))  # Get the first node in the adjacency list
        print(root, end=" ")
        
        visited = set([root])
        
        def dfs_help(u, visited):
            #implement dfs_help
            return
                
        dfs_help(root, visited)
        
    def bfs(self):
        if(not self.adjList): return
        root = next(iter(self.adjList))  # Get the first node in the adjacency list
        print(root, end=" ")

        visited = set([root])

        def bfs_help(level, visited):
            next_level = []
            #implement bfs code (CHALLENGE!)
            return
                
        bfs_help(self.adjList[root], visited)