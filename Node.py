class Node:
    """Class to represent a tree node.
    """
    def __init__ (self, token: str, value: int):
        """Constructor.

        Args:
            token (str): token or word.
            value (int): occurrences of the token.
        """
        self.left = None
        self.right = None
        self.token = token
        self.value = value

    def closeXMLTag(self) -> str:
        """Close XML Tag method.

        Returns:
            str: returns the close tag of the XML elements.
        """
        return f'</{self.token}{self.value}>'

    def insert(self, token: str, value: int) -> None:
        """Insert a new node in the tree.

        Args:
            token (str): token or word.
            value (int): occurrences of the token.
        """
        # If the node has a value
        if self.value:
            # Check if the input value is less than the actual value
            if value < self.value:
                # Then try to insert in the left
                if self.left:
                    self.left.insert(token, value)
                else:
                    self.left = Node(token, value)
            else:
                # Otherwise, try to insert in the right
                if self.right:
                    self.right.insert(token, value)
                else:
                    self.right = Node(token, value)
        # If the node is empty
        else:
            # Insert in the current node
            self.value = value
            self.toke = token

    def openXMLTag(self) -> str:
        """Open XML Tag method.

        Returns:
            str: returns the open tag of the XML elements.
        """
        return f'<{self.token}{self.value}>'

    def __str__(self) -> str:
        """Overriding of the method __str__

        Returns:
            str: returns the string representation of the class
        """
        return f'{self.node.token} {self.node.value}'
