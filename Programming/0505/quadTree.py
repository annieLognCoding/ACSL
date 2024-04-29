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

node = make_tree("5 50 51 36 31 80 51 81 30 80 23 81 30 81 6 80 33 81 31 56 92 11 55 81 6 11 33 11 23 29 31 18 51 60 55 11 55 95 51 11 86 11 86 56 51 95 30 29 54 36 92 18 6 35 92 36 54 80 33 36 30 56 86 35 6 95 31 95 86 95 86 80 86 36 23 56 30 18 31 60 92 56 92 80 55 56 54 18 55 60 23 80 54 35 86 29 54 81 54 56 6 36")
print(node.print_children())

