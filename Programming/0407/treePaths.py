class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def insertLeft(self, n):
        self.left = n
    
    def insertRight(self, n):
        self.right = n


class Tree:
    def __init__(self):
        self.root = None
        self.count = 0
    
    #create a binary tree
    def insert(self, nodeVal):
        if(self.count == 0):
            self.root = Node(nodeVal)
            self.count += 1
            return True
        currNode = self.root
        
        #inserting children nodes
        def insert(nodeVal, currNode):
            #if node <= curr, insert to left
            if(nodeVal <= currNode.val):
                #if left node is taken, travel the left of tree and insert
                if(currNode.left):
                    insert(nodeVal, currNode.left)
                else:
                    currNode.insertLeft(Node(nodeVal))
            #if node > curr, insert to right
            elif(currNode.right):
                #if right node is taken, travel the right of tree and insert
                insert(nodeVal, currNode.right)
            else:
                currNode.insertRight(Node(nodeVal))
        insert(nodeVal, currNode)
        #raise node count of Tree
        self.count += 1
        return True
    
    def dfs(self):
        root = self.root
        def dfs(node):
            print(node.val, end = " ")
            if(node.left):
                dfs(node.left)
            if(node.right):
                dfs(node.right)
        dfs(root)
    

    def findPaths(self):
        root = self.root
        paths = set()
        
        #find all left and right paths that can be travelled by current node
        def findPaths(node, currVal, paths):
            if(node.left):
                paths.add(currVal + node.left.val)
                findPaths(node.left, currVal + node.left.val, paths)
            if(node.right):
                paths.add(currVal + node.right.val)
                findPaths(node.right, currVal + node.right.val, paths)

        
        #combine left and right paths  
        def accumulatePaths(node, currVal, paths):    
            left = set()
            right = set()
            
            #add path: left - curr - right
            paths.add(node.left.val + currVal + node.right.val)
            
            #find all left and right paths that the node's first children can travel
            findPaths(node.left, node.left.val, left)
            findPaths(node.right, node.right.val, right)
            
            for r in right:
                #add left paths - curr - right
                paths.add(node.left.val + currVal + r)
                
            for l in left:
                 #add left - curr - right paths
                paths.add(l + currVal + node.right.val)
                for r in right:
                    #add left paths - curr - right paths
                    paths.add(l + currVal + r)
        
        #find paths for all nodes
        def dfsPaths(node):
            findPaths(node, node.val, paths)
            if(node.left and node.right):
                accumulatePaths(node, node.val, paths)
            if(node.left):
                dfsPaths(node.left)
            if(node.right):
                dfsPaths(node.right)
            
        dfsPaths(root)
        return len(paths)

if __name__ == "__main__":
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    
    for line in Lines:
        
        testTree = Tree()
        nums = line.strip()
        
        for i in nums:
            testTree.insert(int(i))
        print(testTree.findPaths())

    