from collections import deque
import matplotlib.pyplot as plt
import time
import timeit

class tStack:
     def __init__(self):
         self.items = []

     def isempty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

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
      
class lStack:  
    def __init__(self): 
        self.top = None
        self.Size = 0
      
    def isempty(self): 
        if self.top == None: 
            return True
        else: 
            return False
       
    def push(self,item): 
          
        if self.top == None: 
            self.top=Node(item)
            self.Size += 1
              
        else: 
            newnode = Node(item) 
            newnode.setNext(self.top) 
            self.top = newnode
            self.Size += 1
       
    def pop(self): 
          
        if self.isempty(): 
            return None
              
        else:  
            temp = self.top
            self.top = self.top.getNext()
            temp.setNext(None)
            self.Size -=1
            return temp.getData()
        
    def peek(self): 
          
        if self.isempty(): 
            return None
              
        else: 
            return self.top.getData()

    def size(self):
        return self.Size


class dStack:
    def __init__(self):
        self.values = deque()
        self.Size = 0
        
    def isempty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.values.appendleft(item)
        self.Size += 1
       
    def pop(self):
        if self.isempty():
            return None
        else: 
            self.Size -= 1
            return self.values.popleft()

    def peek(self): 
        if self.isempty(): 
            return None    
        else:
            temp = self.values.popleft()
            self.values.appendleft(temp)
            return temp

    def size(self):
        return self.Size

def get_ith1(stack, i):
    if i >= stack.size():
        return None
        
    temp = tStack()
    for k in range(i):
        temp.push(stack.pop())
    toReturn = stack.peek()
    for k in range(i):
        stack.push(temp.pop())
    return toReturn

def get_ith2(stack, i):
    if i >= stack.size():
        return None
        
    temp = lStack()
    for k in range(i):
        temp.push(stack.pop())
    toReturn = stack.peek()
    for k in range(i):
        stack.push(temp.pop())
    return toReturn

def get_ith3(stack, i):
    if i >= stack.size():
        return None
        
    temp = dStack()
    for k in range(i):
        temp.push(stack.pop())
    toReturn = stack.peek()
    for k in range(i):
        stack.push(temp.pop())
    return toReturn

def test1(size, trials):
    my_stack = tStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.time()
        get_ith1(my_stack, size-1)
        end = time.time()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test2(size, trials):
    my_stack = lStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.time()
        get_ith2(my_stack, size-1)
        end = time.time()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

def test3(size, trials):
    my_stack = dStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.time()
        get_ith3(my_stack, size-1)
        end = time.time()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

# Run test functions for sizes from 1 to 50 and store results for plotting
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
plt.xlabel('size of stack')
plt.ylabel('run time')

# Create the legend
plt.legend((alg1, alg2, alg3),('List Stack', 'Linked List Stack', 'Deque Stack'))

# Show the plot
plt.show()
