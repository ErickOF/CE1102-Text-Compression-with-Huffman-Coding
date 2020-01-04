class Tree():
    def __init__ (self, root=None):
        self.root = root

    def __showTree(self, node):
        if node:
            return node.openXMLTag() + self.__showTree(node.left) + self.__showTree(node.right) + node.closeXMLTag()
        return ""

    def toXML(self):
        if self.root == None:
            return "<>"
        return self.__showTree(self.root)

    def __str__(self):
        return self.toXML()

