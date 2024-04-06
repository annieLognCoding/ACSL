from collections import defaultdict 
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

    
    def insert(self, nodeVal):
        if(self.count == 0):
            self.root = Node(nodeVal)
            self.count += 1
            return True
        
        currNode = self.root

        def insert(nodeVal, currNode):
            if(nodeVal <= currNode.val):
                if(currNode.left):
                    insert(nodeVal, currNode.left)
                else:
                    currNode.insertLeft(Node(nodeVal))
            elif(currNode.right):
                insert(nodeVal, currNode.right)
            else:    
                currNode.insertRight(Node(nodeVal))
        
        insert(nodeVal, currNode)
        self.count += 1
        return True
    
    def dfs(self):
        root = self.root
        def dfs(node):
            print(node.val)
            if(node.left):
                dfs(node.left)
            if(node.right):
                dfs(node.right)
        
        dfs(root)

    def findPaths(self):
        root = self.root
        paths = set()

        def findPaths(node, currVal, paths):
            if(node.left):
                paths.add(currVal + node.left.val)
                findPaths(node.left, currVal + node.left.val, paths)   
            if(node.right):
                paths.add(currVal + node.right.val)
                findPaths(node.right, currVal + node.right.val, paths)
            if(node.left and node.right):
                left = set()
                right = set()
                paths.add(node.left.val + currVal + node.right.val)
                findPaths(node.left, node.left.val, left)
                findPaths(node.right, node.right.val, right)
                print("node at: " + str(node.val))
                for r in right:
                    print(r, end=" ")
                    paths.add(node.left.val + currVal + r)
                for l in left:
                    print(l, end=" ")
                    paths.add(l + currVal + node.right.val)
                    for r in right:
                        paths.add(l + currVal + r)

        def dfsPaths(node):
            findPaths(node, node.val, paths)
            if(node.left):
                dfsPaths(node.left)
            if(node.right):
                dfsPaths(node.right)

        dfsPaths(root)
        print(paths)
        return paths



testTree = Tree()
num = "31415926"

for i in num:
    testTree.insert(int(i))

# testTree.dfs()
print(len(testTree.findPaths()))


    