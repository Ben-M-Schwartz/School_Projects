from collections import deque
import matplotlib.pyplot as plt
import time
import timeit

class tQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class lQueue:      
    def __init__(self): 
        self.front = None
        self.back = None
        self.Size = 0
  
    def isEmpty(self): 
        if self.front == None:
            return True
        else:
            return False
       
    def enqueue(self, item): 
        temp = Node(item) 
          
        if self.front == None: 
            self.front = temp
            self.back = temp
            self.Size += 1
            
        else:
            self.back.setNext(temp)
            self.back = temp
            self.Size += 1
   
    def dequeue(self): 
          
        if self.isEmpty(): 
            return None
        else:
            temp = self.front
            self.front = self.front.getNext()
            self.Size -= 1
            return temp.getData()

    def size(self):
        return self.Size


class dQueue:
    def __init__(self):
        self.values = deque()
        self.Size = 0
        
    def isEmpty(self):
        return len(self.values) == 0

    def enqueue(self, item):
        self.values.appendleft(item)
        self.Size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        else: 
            self.Size -= 1
            return self.values.pop()

    def size(self):
        return self.Size

def get_ith1(stack, i):
    if i >= stack.size():
            return None
        
    temp = tQueue()
    for k in range(i):
        temp.enqueue(stack.dequeue())
    toReturn = stack.dequeue()
    temp.enqueue(toReturn)
    for k in range(stack.size()):
        temp.enqueue(stack.dequeue())

    for k in range(temp.size()):
        stack.enqueue(temp.dequeue())
            
    return toReturn

def get_ith2(stack, i):
    if i >= stack.size():
            return None
        
    temp = lQueue()
    for k in range(i):
        temp.enqueue(stack.dequeue())
    toReturn = stack.dequeue()
    temp.enqueue(toReturn)
    for k in range(stack.size()):
        temp.enqueue(stack.dequeue())

    for k in range(temp.size()):
        stack.enqueue(temp.dequeue())
            
    return toReturn

def get_ith3(stack, i):
    if i >= stack.size():
            return None
        
    temp = dQueue()
    for k in range(i):
        temp.enqueue(stack.dequeue())
    toReturn = stack.dequeue()
    temp.enqueue(toReturn)
    for k in range(stack.size()):
        temp.enqueue(stack.dequeue())

    for k in range(temp.size()):
        stack.enqueue(temp.dequeue())
            
    return toReturn

def test1(size, trials):
    my_queue = tQueue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.time()
        get_ith1(my_queue, size-1)
        end = time.time()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test2(size, trials):
    my_queue = lQueue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.time()
        get_ith2(my_queue, size-1)
        end = time.time()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test3(size, trials):
    my_queue = dQueue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.time()
        get_ith3(my_queue, size-1)
        end = time.time()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

# Run test functions for sizes from 1 to 50 and store results for plotting
plt.figure(1)
sizes = range(1, 50, 1)
x1 = [s for s in sizes]
x2 = [s for s in sizes]
x3 = [s for s in sizes]
y1 = [test1(s,100) for s in sizes]
y2 = [test2(s,100) for s in sizes]
y3 = [test3(s,100) for s in sizes]

# Plot the run times against list lengths
colors = ['b', 'c', 'r']
alg1 = plt.scatter(x1, y1, color=colors[0])
alg2 = plt.scatter(x2, y2, color=colors[1])
alg3 = plt.scatter(x3, y3, color=colors[2])

# Label axes
plt.xlabel('size of queue')
plt.ylabel('run time')

# Create the legend
plt.legend((alg1, alg2, alg3),('List Queue', 'Linked List Queue', 'Deque Queue'))

# Show the plot
plt.show()
