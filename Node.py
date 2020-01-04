class Node:
    def __init__ (self, token, value):
        self.__left = None
        self.__right = None
        self.__token = token
        self.__value = value

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def getToken(self):
        return self.__token

    def getValue(self):
        return self.__value

    def setLeft(self, left):
        self.__left = left

    def setRight(self, right):
        self.__right = right

    def setToken(self, token):
        self.__token = token

    def setValue(self, value):
        self.__value = value

    def openXMLTag(self):
        return "<" + self.__token + "-" + str(self.__value) + ">"

    def closeXMLTag(self):
        return "</" + self.__token + "-" + str(self.__value) + ">"

    def __str__(self):
        return node.getToken() + " " + str(node.getValue())

    def insert(self, token, value):
        if self.__value:
            if value < self.__value:
                if self.__left:
                    self.__left.insert(token, value)
                else:
                    self.__left = Node(token, value)
            elif value >= self.__value:
                if self.__right:
                    self.__right.insert(token, value)
                else:
                    self.__right = Node(token, value)
        else:
            self.__value = value
            self.__toke = token
