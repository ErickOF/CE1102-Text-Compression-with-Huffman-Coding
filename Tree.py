from node import *


class Tree():
    def __init__ (self, root=None):
        self.__root = root

    def insert(self, token, value):
        if self.__root:
            self.__root.insert(token, value)
        else:
            self.__root = Node(token, value)

    def __showTree(self, node):
        if node:
            return node.openXMLTag() + self.__showTree(node.getLeft()) + self.__showTree(node.getRight()) + node.closeXMLTag()
        return ""
            
    def __str__(self):
        if self.__root == None:
            return "<>"
        return self.__showTree(self.__root)
    

if __name__ == '__main__':
    tree = Tree()
    print(tree)
    tree.insert('a', 100)
    tree.insert('b', 50)
    tree.insert('e', 300)
    tree.insert('c', 25)
    tree.insert('d', 75)
    tree.insert('f', 200)
    tree.insert('g', 400)
    print(tree)
