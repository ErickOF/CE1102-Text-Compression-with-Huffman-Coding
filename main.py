from node import Node
from tree import Tree
from sorter import Sorter


INPUT_PATH = './files/input/'
OUTPUT_PATH = './files/output/'


def readFile(name, isBinary=False):
    text = ''
    if isBinary:
        with open(name, 'rb') as file:
            text = file.read()
    else:
        with open(name, 'r') as file:
            text = file.read()
    return text

def writeFile(name, text, isBinary=False):
    if isBinary:
        with open(name, 'wb') as file:
            file.write(text)
    else:
        with open(name, 'w') as file:
            file.write(text)

def createFrecuencyDict(words):
    frecuency = {}
    for word in words:
        if word in frecuency:
            frecuency[word] += 1
        else:
            frecuency[word] = 1
    return frecuency

def getCodes(node, code=0):
    if node.left == None:
        return {node.token: bytes([code])}
    else:
        codesLeft = getCodes(node.left, code << 1)
        codesRight = getCodes(node.right, (code << 1) + 1)
        codes = dict(codesLeft, **codesRight)
        return codes

def encodeText(words, codes):
    codedText = bytes()
    for word in words:
        codedText = codedText + codes[word]
    return codedText

def huffmanAlgorithm(words):
    frecuencyDict = createFrecuencyDict(words)
    frecuencyList = [Node(k, v) for k, v in frecuencyDict.items()]

    Sorter().bubble(frecuencyList, f=lambda node: node.value)

    while len(frecuencyList) != 1:
        node1 = frecuencyList.pop(0)
        node2 = frecuencyList.pop(0)

        value = node1.value + node2.value

        newNode = Node('n_', value)
        newNode.left = node1
        newNode.right = node2

        frecuencyList.append(newNode)

        Sorter().bubble(frecuencyList, f=lambda node: node.value)

    tree = Tree(frecuencyList.pop())
    codes = getCodes(tree.root)
    reversedCodes = {v: k for k, v in codes.items()}

    codedText = encodeText(words, codes)

    codesToWrite = (str(reversedCodes) + '\n').encode('utf-8')

    writeFile(OUTPUT_PATH + 'tree.xml', '<?xml version="1.0" encoding="UTF-8" ?>\n' + tree.toXML())
    writeFile(OUTPUT_PATH + 'compressed.ce', codesToWrite + codedText, True)

    return codedText

def decode(text):
    text = text.split(b'\n')
    codes = eval(text[0])
    content = text[1:]

    decodedText = ''
    for line in content:
        for c in line:
            decoded = codes[bytes([c])]
            decodedText = decodedText + decoded
            if decoded != '\n':
                decodedText = decodedText + ' '
    
    return decodedText


if __name__ == '__main__':
    text = readFile(INPUT_PATH + 'test.txt')
    print('Original:\n', text, '\n', sep='')
    text = text.replace('\n', ' \n ')
    words = text.split(' ')

    codedText = huffmanAlgorithm(words)
    print('Coded:\n', codedText, '\n', sep='')

    codedFile = readFile(OUTPUT_PATH + 'compressed.ce', True)
    print('Decoded:\n', decode(codedFile), sep='')

