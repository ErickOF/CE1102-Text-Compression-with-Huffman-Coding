import os
from typing import *

from sorting import Sorting
from tree import Node, Tree


INPUT_PATH: str = './files/input/'
OUTPUT_PATH: str = './files/output/'


def createFrecuencyDict(words: List[str]) -> Dict[str, int]:
    """Create a dictionary with the word occurrences.

    Args:
        words (List[str]): list of words to count.

    Returns:
        Dict[str, int]: dictionary with the word as a key and the occurrences
            as value.
    """
    frecuency = {}

    for word in words:
        if word in frecuency:
            frecuency[word] += 1
        else:
            frecuency[word] = 1

    return frecuency

def decode(text: str) -> str:
    """Function to decode an input text.

    Args:
        text (str): text to decode.

    Returns:
        str: decoded text.
    """
    text_list: List[bytes] = text.split(b'\n')
    # Get the dictionary of tokens:occurences
    codes: Dict[str, bytes] = eval(text_list[0])
    # Get the encoded content
    content: List[bytes] = text_list[1:]

    decodedText: str = ''

    # Decode each line of the file
    for line in content:
        # Decode each caracter in the line
        for c in line:
            # Decode the character
            decoded = codes[bytes([c])]
            # Add to the decoded text
            decodedText = decodedText + decoded

            if decoded != '\n':
                decodedText = decodedText + ' '
    
    return decodedText

def encodeText(words: List[str], codes: List[bytes]) -> bytes:
    """Enconde the text as bytes.

    Args:
        words (List[str]): list of words to encode.
        codes (List[bytes]): list of codes to encode the words.

    Returns:
        bytes: byte array for the encoded text.
    """
    codedText = bytes()

    for word in words:
        codedText = codedText + codes[word]

    return codedText

def getCodes(node: Node, code:int=0) -> Dict[str, bytes]:
    """Extract the list of codes from the tree root.

    Args:
        node (Node): root of the tree
        code (int, optional): accumulator for the code. Defaults to 0.

    Returns:
        Dict[str, bytes]: dictionary with the token as key and the code as
            value.
    """
    # If left is empty, there are not more children
    if node.left == None:
        # Then return the token:code
        return {node.token: bytes([code])}
    else:
        # Move left and add a zero
        codesLeft = getCodes(node.left, code << 1)
        # Move right and add a one
        codesRight = getCodes(node.right, (code << 1) + 1)
        # Join the two dictionaries
        codes = dict(codesLeft, **codesRight)

        return codes

def readFile(name: str, isBinary:bool=False) -> str:
    """Read the input file.

    Args:
        name (str): name of the file to open.
        isBinary (bool, optional): Indicates if the file is binary or not.
            Defaults to False.

    Returns:
        str: content of the file.
    """
    # Select file mode
    mode: str = 'rb' if isBinary else 'r'
    # Content of the file
    text: str = ''

    # Read the file
    with open(name, mode) as file:
        text = file.read()

    return text

def writeFile(name: str, text: str, isBinary:bool=False) -> None:
    """Write into a file.

    Args:
        name (str): name of the file to write.
        text (str): content to write.
        isBinary (bool, optional): Indicates if the file is binary or not.
            Defaults to False.
    """
    # Select file mode
    mode: str = 'wb' if isBinary else 'w'

    # Write the content
    with open(name, mode) as file:
        file.write(text)


def huffmanAlgorithm(words: List[str]) -> str:
    """Apply Huffman Algorithm

    Args:
        words (List[str]): words to encode

    Returns:
        str: encoded text
    """
    # Get the frequency dictionary
    frecuencyDict: Dict[str, int] = createFrecuencyDict(words)
    # Convert to a list of nodes
    frecuencyList = [Node(k, v) for k, v in frecuencyDict.items()]

    # Sorting the list of nodes
    Sorting().bubble(frecuencyList, f=lambda node: node.value)

    # Build the tree
    while len(frecuencyList) != 1:
        node1: Node = frecuencyList.pop(0)
        node2: Node = frecuencyList.pop(0)

        value: int = node1.value + node2.value

        newNode: Node = Node('n_', value)
        newNode.left = node1
        newNode.right = node2

        frecuencyList.append(newNode)

        Sorting().bubble(frecuencyList, f=lambda node: node.value)

    # Create the Huffman tree
    tree: Tree = Tree(frecuencyList.pop())
    # Get the codes from the tree
    codes: Dict[str, bytes] = getCodes(tree.root)
    # Exchange the str and bytes
    reversedCodes: Dict[bytes, str] = {v: k for k, v in codes.items()}

    # Encode input text
    encodedText: str = encodeText(words, codes)

    # Converts to UTF-8
    codesToWrite = f'{reversedCodes}\n'.encode('utf-8')

    # Write XML output file
    writeFile(
        os.path.join(OUTPUT_PATH, 'tree.xml'),
        f'<?xml version="1.0" encoding="UTF-8" ?>\n{tree.toXML()}'
    )
    # Write the enconded text into the output file
    writeFile(
        os.path.join(OUTPUT_PATH, 'compressed.ce'),
        codesToWrite + encodedText,
        True
    )

    return encodedText


if __name__ == '__main__':
    # Get the input text
    text: str = readFile(INPUT_PATH + 'test.txt')
    print('Original:\n', text, '\n', sep='')

    # Extract the words
    text = text.replace('\n', ' \n ')
    words: List[str] = text.split(' ')

    # Compress the text
    encodedText: str = huffmanAlgorithm(words)
    print(f'Coded:\n{encodedText}\n')

    # Decompress the text
    encodedFile: str = readFile(OUTPUT_PATH + 'compressed.ce', True)
    print(f'Decoded:\n{decode(encodedFile)}')
