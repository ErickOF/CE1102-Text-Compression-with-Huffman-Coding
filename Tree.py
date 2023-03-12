from node import Node

class Tree():
    """Class that represents a binary tree.
    """
    def __init__ (self, root:Node=None):
        """Constructor of the class.

        Args:
            root (Node, optional): Root of the tree. Defaults to None.
        """
        self.root = root

    def toXML(self) -> str:
        """Convert Tree to XML.

        Returns:
            str: string representing the XML output.
        """
        if self.root == None:
            return '<>'

        return self.__showTree(self.root)

    def __showTree(self, node: Node) -> str:
        """Method to return a string representation of the tree.

        Args:
            node (Node): root of the tree.

        Returns:
            str: representation of the tree.
        """
        if node:
            return f'{node.openXMLTag()}{self.__showTree(node.left)}{self.__showTree(node.right)}{node.closeXMLTag()}'

        return ''

    def __str__(self) -> str:
        """Overriding method __str__.

        Returns:
            str: returns the string representation of the class.
        """
        return self.toXML()
