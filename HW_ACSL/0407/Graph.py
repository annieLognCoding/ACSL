from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)
 
    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)
    #{u: [v]}
    
    def isLeaf(self, u):
        return len(self.adjList[u]) == 0
    
    def dfs(self):
        if(not self.adjList): return
        root = next(iter(self.adjList))  # Get the first node in the adjacency list
        print(root, end=" ")
        
        visited = set([root])
        
        def dfs_help(u, visited):
            for v in self.adjList[u]:
                if(v not in visited):
                    print(v, end=" ")
                    visited.add(v)
                    dfs_help(v, visited)
                
        dfs_help(root, visited)
        
    def bfs(self):
        if(not self.adjList): return
        root = next(iter(self.adjList))  # Get the first node in the adjacency list
        print(root, end=" ")

        visited = set([root])

        def bfs_help(level, visited):
            next_level = []
            for v in level:
                if(v not in visited):
                    print(v, end=" ")
                    visited.add(v)
                    next_level.extend([nextnode for nextnode in self.adjList[v] if nextnode not in visited])
            len(next_level) and bfs_help(next_level, visited)
                
        bfs_help(self.adjList[root], visited)

def bfs_test():
    # Test case 1: Empty Graph
    print("Test case 1: Empty Graph")
    g1 = Graph()
    # No edges to add
    g1.bfs()  # Assuming a starting node, but no output expected

    # Test case 2: Single Node
    print("\nTest case 2: Single Node")
    g2 = Graph()
    # No edges, just a single node
    g2.bfs()

    # Test case 3: Linear Graph
    print("\nTest case 3: Linear Graph")
    g3 = Graph()
    g3.addEdge(1, 2)
    g3.addEdge(2, 3)
    g3.addEdge(3, 4)
    g3.bfs()

    # Test case 4: Star Graph
    print("\nTest case 4: Star Graph")
    g4 = Graph()
    for i in range(2, 6):
        g4.addEdge(1, i)
    g4.bfs()

    # Test case 5: Binary Tree
    print("\nTest case 5: Binary Tree")
    g5 = Graph()
    g5.addEdge(1, 2)
    g5.addEdge(1, 3)
    g5.addEdge(2, 4)
    g5.addEdge(2, 5)
    g5.addEdge(3, 6)
    g5.addEdge(3, 7)
    g5.bfs()
    
    # Test case 6: Graph with a Cycle
    print("\nTest case 6: Graph with a Cycle")
    g6 = Graph()
    g6.addEdge(1, 2)
    g6.addEdge(2, 3)
    g6.addEdge(3, 1)  # Creates a cycle
    g6.addEdge(3, 4)
    g6.bfs()

    # Test case 7: Disconnected Graph
    print("\nTest case 7: Disconnected Graph")
    g7 = Graph()
    g7.addEdge(1, 2)
    g7.addEdge(3, 4)
    g7.addEdge(4, 5)
    g7.bfs()  # Starting from a node in the first component

    # Test case 8: Complete Graph
    print("\nTest case 8: Complete Graph")
    g8 = Graph()
    # Adding all possible edges for a complete graph with 4 nodes
    for i in range(1, 5):
        for j in range(i + 1, 5):
            g8.addEdge(i, j)
            g8.addEdge(j, i)
    g8.bfs()

    # Test case 9: Larger Binary Tree
    print("\nTest case 9: Larger Binary Tree")
    g9 = Graph()
    # Constructing a binary tree where each node n has children at 2n and 2n+1
    for n in range(1, 8):  # Only going up to 7 to add children within 1-15
        g9.addEdge(n, 2 * n)
        g9.addEdge(n, 2 * n + 1)
    g9.bfs()

    # Test case 10: Graph with Parallel Edges and Self-loop
    print("\nTest case 10: Graph with Parallel Edges and Self-loop")
    g10 = Graph()
    g10.addEdge(1, 2)
    g10.addEdge(2, 3)
    g10.addEdge(3, 2)  # Parallel edge back to 2
    g10.addEdge(3, 3)  # Self-loop at 3
    g10.addEdge(2, 4)
    g10.bfs()
    
def dfs_test():
    # Test case 1: Empty Graph
    print("Test case 1: Empty Graph")
    g1 = Graph()
    g1.dfs()

    # Test case 2: Single Node
    print("\nTest case 2: Single Node")
    g2 = Graph()
    g2.addEdge(1, 1)  # Adding a self-loop to see if it handles this case.
    g2.dfs()

    # Test case 3: Linear Graph
    print("\nTest case 3: Linear Graph")
    g3 = Graph()
    g3.addEdge(1, 2)
    g3.addEdge(2, 3)
    g3.addEdge(3, 4)
    g3.dfs()

    # Test case 4: Simple Cycle
    print("\nTest case 4: Simple Cycle")
    g4 = Graph()
    g4.addEdge(1, 2)
    g4.addEdge(2, 3)
    g4.addEdge(3, 1)  # Creating a cycle
    g4.dfs()

    # Test case 5: Tree Structure
    print("\nTest case 5: Tree Structure")
    g5 = Graph()
    g5.addEdge(1, 2)
    g5.addEdge(1, 3)
    g5.addEdge(2, 4)
    g5.addEdge(2, 5)
    g5.addEdge(3, 6)
    g5.addEdge(3, 7)
    g5.dfs()

    # Test case 6: Disconnected Graph
    print("\nTest case 6: Disconnected Graph")
    g6 = Graph()
    g6.addEdge(1, 2)
    g6.addEdge(2, 3)
    # Disconnected component
    g6.addEdge(4, 5)
    g6.addEdge(5, 6)
    g6.dfs()  # Should only traverse the component containing the root node.

    # Test case 7: Graph with Back Edges
    print("\nTest case 7: Graph with Back Edges")
    g7 = Graph()
    g7.addEdge(1, 2)
    g7.addEdge(2, 3)
    g7.addEdge(3, 4)
    g7.addEdge(4, 2)  # Adding a back edge to create a cycle.
    g7.dfs()

if __name__ == "__main__":
    dfs_test()
    