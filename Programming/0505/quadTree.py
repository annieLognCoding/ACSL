class QuadTree():
    def __init__(self):
        self.root = None
        self.count = 0
        self.nodes = []

    def insertNode(self, coordinates):
        [x, y] = coordinates
        self.count += 1
        node = Node(self.count, x, y)
        if(not self.root):
            self.root = node
        else:
            self.root.insertChild(node)
        self.nodes.append(node)

    def getNode(self, k):
        return self.nodes[k-1]

class Node():
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y
        self.First = None
        self.Second = None
        self.Third = None
        self.Fourth = None

    def insertChild(self, node):
        
        x, y = node.x, node.y
        if(x > self.x and y > self.y):
            if(self.First):
                firstChild = self.First
                firstChild.insertChild(node)
            else:
                self.First = node
        elif(x <= self.x and y > self.y):
            if(self.Second):
                secondChild = self.Second
                secondChild.insertChild(node)
            else:
                self.Second = node
        elif(x <= self.x and y <= self.y):
            if(self.Third):
                thirdChild = self.Third
                thirdChild.insertChild(node)
            else:
                self.Third = node
        elif(x > self.x and y <= self.y):
            if(self.Fourth):
                fourthChild = self.Fourth
                fourthChild.insertChild(node)
            else:
                self.Fourth = node
    
    def __str__(self):
        return str(self.key)
    
    def print_children(self):
        result = ""
        if(self.First):
            result += str(self.First)
        else:
            result += str(0)
        
        if(self.Second):
            result += str(self.Second)
        else:
            result += str(0)

        if(self.Third):
            result += str(self.Third)
        else:
            result += str(0)

        if(self.Fourth):
            result += str(self.Fourth)
        else:
            result += str(0)
        return result

def make_tree(input_text):
    tree = QuadTree()
    split_text = input_text.split(" ")
    k = int(split_text[0])
    n = int(split_text[1])
    nodes = split_text[2:]
    for i in range(0, len(nodes) - 1, 2):
        [x, y] = nodes[i: i+2]
        tree.insertNode([int(x), int(y)])
    return tree.getNode(k)

node = make_tree("9 15 4 2 8 5 10 -3 6 -7 5 -6 6 3 -5 -7 8 -4 0 -2 2 1 7 -11 -10 -9 1 0 -3 -5 -1 1")
print(node.print_children())


