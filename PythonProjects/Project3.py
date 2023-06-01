def insertionSort(myList):
    sortedList = [myList[0]] + [None]*(len(myList)-1)
    
    for i in range(1, len(myList)):
        j = i-1
        while j>=0 :
            if sortedList[j] > myList[i]:
                sortedList[j+1] = sortedList[j]
                j-=1
            else:
                break

        sortedList[j+1] = myList[i]
                
    return sortedList

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList)//2

        left = mergeSort(myList[:mid])
        right = mergeSort(myList[mid:])

        i = 0
        j = 0
        k = 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i +=1
                k +=1
            else:
                myList[k] = right[j]
                j +=1
                k +=1
        while i<len(left):
            myList[k] = left[i]
            i +=1
            k +=1
        while j<len(right):
            myList[k] = right[j]
            j +=1
            k +=1

    return myList

def stoogeSortFunction(myList, first, last):
    
    if myList[first] > myList[last]:
        temp = myList[first]
        myList[first] = myList[last]
        myList[last] = temp
        
    if last-first+1 > 2:

        oneThird = (last-first+1)//3

        stoogeSortFunction(myList, first, last-oneThird)
        stoogeSortFunction(myList, first+oneThird, last)
        stoogeSortFunction(myList, first, last-oneThird)

    return myList

def stoogeSort(myList):
    return stoogeSortFunction(myList, 0, len(myList)-1)

#https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def sortedList(self, myList):
        if self.left:
            self.left.sortedList(myList)
        myList.append(self.data)
        if self.right:
            self.right.sortedList(myList)

        return myList

def binaryInsertionSort(myList):
    tree = Tree(myList[0])
    
    for i in range(1, len(myList)):
        tree.insert(myList[i])

    myList = tree.sortedList([])

    return myList


#https://www.geeksforgeeks.org/min-heap-in-python/
#https://github.com/python/cpython/blob/3.9/Lib/heapq.py


"""
O(n)
def heapify(x):
    #Transform list into a heap, in-place, in O(len(x)) time.
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n//2)):
        _siftup(x, i)
        
O(logn)
def heappush(heap, item):
    #Push item onto heap, maintaining the heap invariant.
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

O(logn)
def heappop(heap):
    #Pop the smallest item off the heap, maintaining the heap invariant.
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem"""

"""def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)"""

from heapq import heapify, heappush, heappop

def heapSort(myList):
    heap = []
    heapify(heap)

    for i in range(len(myList)):
        heappush(heap, myList[i])

    for i in range(len(myList)):
        myList[i] = heappop(heap)

    return myList


#https://docs.python.org/3/library/random.html
import random
def bogoSort(myList):

    keepGoing = True
    while keepGoing:
        myList = random.sample(myList, len(myList))
        isSorted = True
        for i in range(len(myList)-1):
            if myList[i+1] < myList[i]:
                isSorted = False
        if isSorted == True:
            keepGoing = False

    return myList

def quickSortHelper(myList, start, end):
    if end-start > 0:

        pivot = myList[start]

        stop = False

        i = start+1
        j = end
        while stop == False:
            while myList[i] < pivot and i<j:
                i +=1

            while myList[j] > pivot and j>i:
                j -=1

            if i<j and myList[i] > pivot and myList[j] < pivot:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
                
            else:
                if myList[j] < myList[start]:
                    temp = myList[start]
                    myList[start] = myList[j]
                    myList[j] = temp
                stop = True

        quickSortHelper(myList, start, j-1)
        quickSortHelper(myList, i, end)

    return myList

def quickSort(myList):
    return quickSortHelper(myList, 0, len(myList)-1)

import matplotlib.pyplot as plt
import time
import timeit

def graph():
     plt.figure(2)
     sizes = range(1, 100, 1)
     #x1 = [s for s in sizes]
     #x2 = [s for s in sizes]
     #x3 = [s for s in sizes]
     #x4 = [s for s in sizes]
     #x5 = [s for s in sizes]
     #x6 = [s for s in sizes]
     #x7 = [s for s in sizes]
     #y1 = [test1(s,100) for s in sizes]
     #y2 = [test2(s,100) for s in sizes]
     #y3 = [test3(s,100) for s in sizes]
     #y4 = [test4(s,100) for s in sizes]
     #y5 = [test5(s,100) for s in sizes]
     #y6 = [test6(s,100) for s in sizes]
     #y7 = [test7(s,100) for s in sizes]

     # Plot the run times against list lengths
     colors = ['b', 'c', 'r', 'g', 'm', 'y', 'k']
     #alg1 = plt.scatter(x1, y1, color=colors[0])
     #alg2 = plt.scatter(x2, y2, color=colors[1])
     #alg3 = plt.scatter(x3, y3, color=colors[2])
     #alg4 = plt.scatter(x4, y4, color=colors[3])
     #alg5 = plt.scatter(x5, y5, color=colors[4])
     #alg6 = plt.scatter(x6, y6, color=colors[5])
     #alg7 = plt.scatter(x7, y7, color=colors[6])

     # Label axes
     plt.xlabel('List Size')

     # Create the legend
     """plt.legend((alg1, alg2, alg3, alg4, alg5, alg7),('Insertion Sort', \
                                    'Merge Sort', \
                                    'Binary Insertion Sort', \
                                    'Stooge Sort', \
                                    'Heap Sort', \
                                    'Quick Sort'))"""
          
     plt.title("Time Complexity of Sorting Algorithms")

     # Show the plot
     plt.show()

def test1(size, trials):
    alist = []
    time1 = 0
    for i in (range(size)):
        alist.append(size-i)

    for i in range(trials):
        start = time.perf_counter()
        insertionSort(alist)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test2(size, trials):
    alist = []
    time1 = 0
    for i in (range(size)):
        alist.append(size-i)

    for i in range(trials):
        start = time.perf_counter()
        mergeSort(alist)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1



def test3(size, trials):
    alist = []
    time1 = 0
    for i in (range(size)):
        alist.append(size-i)

    for i in range(trials):
        start = time.perf_counter()
        binaryInsertionSort(alist)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1



def test4(size, trials):
    alist = []
    time1 = 0
    for i in (range(size)):
        alist.append(size-i)

    for i in range(trials):
        start = time.perf_counter()
        stoogeSort(alist)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test5(size, trials):
    alist = []
    time1 = 0
    for i in (range(size)):
        alist.append(size-i)

    for i in range(trials):
        start = time.perf_counter()
        heapSort(alist)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test6(size, trials):
    alist = []
    time1 = 0
    for i in (range(size)):
        alist.append(size-i)

    for i in range(trials):
        start = time.perf_counter()
        bogoSort(alist)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test7(size, trials):
    alist = []
    time1 = 0
    for i in (range(size)):
        alist.append(size-i)

    for i in range(trials):
        start = time.perf_counter()
        quickSort(alist)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1
