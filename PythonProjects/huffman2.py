import heapq
import itertools

'''
    heapq library of python - https://docs.python.org/2/library/heapq.html
'''

pq = []                         # list of entries arranged in a heap
counter = itertools.count()     # unique sequence count
            
def charFrequency(string):
    frequencies = {}
    for char in string:
        if char  not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    return frequencies

class Node():
    def __init__(self, d, f):
        self.data = d
        self.frequency = f
        self.parent = None
        self.left = None
        self.right = None

def huffman(freqDict):
    for char in freqDict:
        node = Node(char, freqDict.get(char))
        count = next(counter)
        entry = [node.frequency, count, node]
        heapq.heappush(pq, entry)

    while(len(pq) > 1):
        priority, count, task = heapq.heappop(pq)
        left = task
        priority, count, task = heapq.heappop(pq)
        right = task
        freq = left.frequency + right.frequency
        z = Node(None, freq)
        left.parent = z
        right.parent = z
        z.left = left
        z.right = right
        count = next(counter)
        entry = [z.frequency, count, z]
        heapq.heappush(pq, entry)

    priority, count, task = heapq.heappop(pq)

    return task

def decode(code, tree):
    phrase = ""
    node = tree
    for bit in code:
        if bit == '0':
            if node.left == None:
                phrase = phrase + node.data
                node = tree
            else:
                node = node.left
        else:
            if node.right == None:
                phrase = phrase + node.data
                node = tree
            else:
                node = node.right

    return phrase

Search = Node('0', 0)

def search(root, char):
    if(root != None):
        if root.left.data == char:
            Search = root.left
        if root.right.data == char:
            Search = root.right
        search(root.left, char)
        search(root.right, char)

def encode(string, tree):
    for char in string:
        search(tree, char)
        node = Search
        while node != tree:
                bits = bits + '0'
                node = node.parent
                bits = bits + '1'
                none = node.parent
                

tree = huffman(charFrequency("i've got the rhythm - the algorithm rythm"))
print(decode("0000010001101011010100101010111010101", tree))
search(tree, 'r')
print(Search.data)
