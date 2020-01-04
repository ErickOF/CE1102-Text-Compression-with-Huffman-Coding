class Node:
    def __init__ (self, token, value):
        self.left = None
        self.right = None
        self.token = token
        self.value = value

    def openXMLTag(self):
        return "<" + self.token + "" + str(self.value) + ">"

    def closeXMLTag(self):
        return "</" + self.token + "" + str(self.value) + ">"

    def __str__(self):
        return node.token + " " + str(node.value)

    def insert(self, token, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(token, value)
                else:
                    self.left = Node(token, value)
            elif value >= self.value:
                if self.right:
                    self.right.insert(token, value)
                else:
                    self.right = Node(token, value)
        else:
            self.value = value
            self.toke = token
