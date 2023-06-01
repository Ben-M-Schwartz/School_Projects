from collections import deque
import matplotlib.pyplot as plt
import time
import timeit

class Queue:
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

class Stack:
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

def pushBottom(stack, item):
    temp = Stack()
    for i in range(stack.size()):
        temp.push(stack.pop())
    stack.push(item)
    for i in range(temp.size()):
        stack.push(temp.pop())

def popBottom(stack):
    temp = Stack()
    for i in range(stack.size()-1):
        temp.push(stack.pop())
    toReturn = stack.pop()
    for i in range(temp.size()):
        stack.push(temp.pop())

    return toReturn

def insertFront(queue, item):
    temp = Queue()
    for i in (range(queue.size())):
        temp.enqueue(queue.dequeue())
    queue.enqueue(item)
    for i in (range(temp.size())):
        queue.enqueue(temp.dequeue())

def removeBack(queue):
    temp = Queue()
    for i in (range(queue.size() - 1)):
        temp.enqueue(queue.dequeue())
    toReturn = queue.dequeue()
    for i in (range(temp.size())):
        queue.enqueue(temp.dequeue())


def test1_1(size, trials):
    my_stack = Stack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.time()
        my_stack.push(5)
        end = time.time()
        time1 += (end - start)
        my_stack.pop()

    avgTime = time1/trials

    return time1
        

def test1_2(size, trials):
    my_queue = Queue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.time()
        insertFront(my_queue, 5)
        end = time.time()
        time1 += (end - start)
        my_queue.dequeue()

    avgTime = time1/trials

    return time1
        

# Run test functions for sizes from 1 to 50 and store results for plotting
plt.figure(1)
sizes = range(1, 50, 1)
x1 = [s for s in sizes]
x2 = [s for s in sizes]
y1 = [test1_1(s,100) for s in sizes]
y2 = [test1_2(s,100) for s in sizes]  

# Plot the run times against list lengths
colors = ['b', 'c']
alg1 = plt.scatter(x1, y1, color=colors[0])
alg2 = plt.scatter(x2, y2, color=colors[1])

# Label axes
plt.xlabel('size')
plt.ylabel('run time')

# Create the legend
plt.legend((alg1, alg2),('Stack', 'Queue'))

# Show the plot
plt.show()

def test2_1(size, trials):
    my_stack = Stack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.time()
        my_stack.pop()
        end = time.time()
        time1 += (end - start)
        my_stack.push(5)

    avgTime = time1/trials

    return time1
        

def test2_2(size, trials):
    my_queue = Queue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.time()
        my_queue.dequeue()
        end = time.time()
        time1 += (end - start)
        my_queue.enqueue(5)

    avgTime = time1/trials

    return time1
        

# Run test functions for sizes from 1 to 50 and store results for plotting
plt.figure(2)
sizes = range(1, 50, 1)
x1 = [s for s in sizes]
x2 = [s for s in sizes]
y1 = [test2_1(s,100) for s in sizes]
y2 = [test2_2(s,100) for s in sizes]  

# Plot the run times against list lengths
colors = ['b', 'c']
alg1 = plt.scatter(x1, y1, color=colors[0])
alg2 = plt.scatter(x2, y2, color=colors[1])

# Label axes
plt.xlabel('size')
plt.ylabel('run time')

# Create the legend
plt.legend((alg1, alg2),('Stack', 'Queue'))

# Show the plot
plt.show()


def test3_1(size, trials):
    my_stack = Stack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.time()
        pushBottom(my_stack, 5)
        end = time.time()
        time1 += (end - start)
        my_stack.pop()

    avgTime = time1/trials

    return time1
        

def test3_2(size, trials):
    my_queue = Queue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.time()
        my_queue.enqueue(5)
        end = time.time()
        time1 += (end - start)
        my_queue.dequeue()

    avgTime = time1/trials

    return time1
        

# Run test functions for sizes from 1 to 50 and store results for plotting
plt.figure(3)
sizes = range(1, 50, 1)
x1 = [s for s in sizes]
x2 = [s for s in sizes]
y1 = [test3_1(s,100) for s in sizes]
y2 = [test3_2(s,100) for s in sizes]  

# Plot the run times against list lengths
colors = ['b', 'c']
alg1 = plt.scatter(x1, y1, color=colors[0])
alg2 = plt.scatter(x2, y2, color=colors[1])

# Label axes
plt.xlabel('size')
plt.ylabel('run time')

# Create the legend
plt.legend((alg1, alg2),('Stack', 'Queue'))

# Show the plot
plt.show()

def test4_1(size, trials):
    my_stack = Stack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.time()
        popBottom(my_stack)
        end = time.time()
        time1 += (end - start)
        my_stack.push(5)

    avgTime = time1/trials

    return time1
        

def test4_2(size, trials):
    my_queue = Queue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.time()
        removeBack(my_queue)
        end = time.time()
        time1 += (end - start)
        my_queue.enqueue(5)

    avgTime = time1/trials

    return time1
        

# Run test functions for sizes from 1 to 50 and store results for plotting
plt.figure(4)
sizes = range(1, 50, 1)
x1 = [s for s in sizes]
x2 = [s for s in sizes]
y1 = [test4_1(s,100) for s in sizes]
y2 = [test4_2(s,100) for s in sizes]  

# Plot the run times against list lengths
colors = ['b', 'c']
alg1 = plt.scatter(x1, y1, color=colors[0])
alg2 = plt.scatter(x2, y2, color=colors[1])

# Label axes
plt.xlabel('size')
plt.ylabel('run time')

# Create the legend
plt.legend((alg1, alg2),('Stack', 'Queue'))

# Show the plot
plt.show()
