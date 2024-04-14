# Class representing a node of the BST
class node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.count = 1

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def hasSingleChild(self):
        return (self.leftChild or self.rightChild) and not(self.rightChild and self.leftChild)

# Traverse through all nodes and add counts of those w/ single child
    def preOrderTraversal(self, sumCounter):
        if self:
            if self.hasLeftChild():
                sumCounter = self.leftChild.preOrderTraversal(sumCounter)
            if self.hasRightChild():
                sumCounter = self.rightChild.preOrderTraversal(sumCounter)
            if self.hasSingleChild():
                return sumCounter + self.count
            else:
                return sumCounter

# Class representing the BST with insert and search functions
class binarySearchTree:
    def __init__(self):
        self.root = None

    def insertRoot(self, key):
        if self.root:
            self.insertNode(key, self.root)
        else:
            self.root = node(key)

    def insertNode(self, key, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.insertNode(key, currentNode.leftChild)
            else:
                currentNode.leftChild = node(key, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self.insertNode(key, currentNode.rightChild)
            else:
                currentNode.rightChild = node(key, parent=currentNode)
        else:
            currentNode.count += 1

    def search(self, key):
        if self.root:
            result = self.searchNode(key, self.root)
            if result:
                return result.count
            else:
                return None
        else:
            return None

    def searchNode(self, key, currentNode):

        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self.searchNode(key, currentNode.leftChild)
        else:
            return self.searchNode(key, currentNode.rightChild)

    def sumCounts(self):

        if self.root:
            return self.root.preOrderTraversal(0)

# Collect inputs for function call
def main():

    test1 = input("Enter string: ")
    findSumCounters(test1)

    test2 = input("Enter string: ")
    findSumCounters(test2)

    test3 = input("Enter string: ")
    findSumCounters(test3)

    test4 = input("Enter string: ")
    findSumCounters(test4)

    test5 = input("Enter string: ")
    findSumCounters(test5)

# Create BST and find sum of counts for single-child nodes
def findSumCounters(string):

    letters = string.upper()
    tree = binarySearchTree()

    for letter in letters:
        if letter.isalpha():
            tree.insertRoot(letter)

    print(tree.sumCounts())


if __name__ == "__main__":
    main()

    # 15 abracadabracabob
    # 9  American Computer Science League
    # 23 Python and Java are programming languages
    # 18 Python and Java and java and python
    # 9  the quick brown fox jumped over the lazy river

