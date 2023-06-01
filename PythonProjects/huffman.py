import heapq
import itertools
'''
    heapq library of python - https://docs.python.org/2/library/heapq.html
'''

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

def inorder(root):
    if(root != None):
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def search(root, char):
    if(root != None):
        search(root.left, char)
        if root.data == char:
            return root
        search(root.right, char)
        
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
        'Add a new task or update the priority of an existing task'
        add_task(node, node.frequency)

    while(len(pq) > 1):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        left = pop_task()
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        right = pop_task()
        freq = left.frequency + right.frequency
        z = Node(None, freq)
        left.parent = z
        right.parent = z
        z.left = left
        z.right = right
        'Add a new task or update the priority of an existing task'
        add_task(z, z.frequency)

    return pop_task()

Search = Node('0', 0)

def search(root, char):
    if(root != None):
        search(root.left, char)
        if(root.data == char):
            Search = root
        search(root.right, char)

def encode(string, tree):
    bits = ""
    for char in string:
        search(tree, char)
        node = Search
        while node != tree:
            if(node == node.parent.left):
                bits = bits + '0'
                node = node.parent
            else:
                bits = bits + '1'
                node = node.parent

tree = huffman(charFrequency("i've got the rhythm - the algorithm rythm"))
search(tree, 'l')
print(Search.data)
inorder(tree)
