class Node:
    def __init__ (self, token, repetions):
        self.__left = None
        self.__right = None
        self.__token = token
        self.__repetions = repetions

    def getToken(self):
        return self.__token

    def getRepetions(self):
        return self.__repetions

    def setToken(self, token):
        self.__token = token

    def setRepetions(self, repetions):
        self.__repetions = repetions

    def isLeaf(self):
        return self.__lef != None

    def insert(self, node):
        if self.__left == None:
            self.__left = node
        elif self.__right == None:
            self.__right = node

    def openXMLTag(self):
        return "<" + self.__token + "-" + str(self.__repetions) + ">"

    def closeXMLTag(self):
        return "</" + self.__token + "-" + str(self.__repetions) + ">"

    def printNodesList(nodes):
        for node in nodes:
            print(node.getToken() + " " + str(node.getRepetions()))
