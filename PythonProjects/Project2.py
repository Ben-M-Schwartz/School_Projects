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
         if self.isempty():
              return None
         else:
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
        if self.Size == 0: 
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
            return self.top.getData()

    def size(self):
        return self.Size

class dStack:
    def __init__(self):
        self.values = deque()
        
    def isempty(self):
        if self.values:
            return False
        else:
            return True

    def push(self, item):
        self.values.append(item)
       
    def pop(self):
        if self.isempty():
            return None
        else: 
            return self.values.pop()

    def peek(self):
         return self.values[-1]

    def size(self):
        return len(self.values)
     
def graph(fun, title, counter, stackOrQueue):
     plt.figure(counter)
     sizes = range(1, 50, 1)
     x1 = [s for s in sizes]
     x2 = [s for s in sizes]
     x3 = [s for s in sizes]
     y1 = [fun(s,100, 1) for s in sizes]
     y2 = [fun(s,100, 2) for s in sizes]
     y3 = [fun(s,100, 3) for s in sizes]

     # Plot the run times against list lengths
     colors = ['b', 'c', 'r']
     alg1 = plt.scatter(x1, y1, color=colors[0])
     alg2 = plt.scatter(x2, y2, color=colors[1])
     alg3 = plt.scatter(x3, y3, color=colors[2])

     # Label axes
     if stackOrQueue == 1:
          plt.xlabel('stack size')
     else:
          plt.xlabel('queue size')
     plt.ylabel('run time')

     # Create the legend
     if stackOrQueue == 1:
          plt.legend((alg1, alg2, alg3),('List Stack', 'Linked List Stack', 'Deque Stack'))
     else:
          plt.legend((alg1, alg2, alg3),('List Queue', 'Linked List Queue', 'Deque Queue'))
          
     plt.title(title)

     # Show the plot
     plt.show()

def test1(size, trials, stacktype):
    if stacktype == 1:
         my_stack = tStack()
    elif stacktype == 2:
         my_stack = lStack()
    else:
         my_stack = dStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        my_stack.isempty()
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

graph(test1, "isEmpty() Comparison for Stacks", 1, 1)

def test2(size, trials, stacktype):
    if stacktype == 1:
         my_stack = tStack()
    elif stacktype == 2:
         my_stack = lStack()
    else:
         my_stack = dStack()
         
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        my_stack.push(5)
        end = time.perf_counter()
        time1 += (end - start)
        my_stack.pop()

    avgTime = time1/trials

    return time1

graph(test2, "Push() Comparison for Stacks", 2, 1)

def test3(size, trials, stacktype):
    if stacktype == 1:
         my_stack = tStack()
    elif stacktype == 2:
         my_stack = lStack()
    else:
         my_stack = dStack()
         
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        my_stack.pop()
        end = time.perf_counter()
        time1 += (end - start)
        my_stack.push(5)

    avgTime = time1/trials

    return time1

graph(test3, "Pop() Comparison for Stacks", 3, 1)

def test4(size, trials, stacktype):
    if stacktype == 1:
         my_stack = tStack()
    elif stacktype == 2:
         my_stack = lStack()
    else:
         my_stack = dStack()
     
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        my_stack.peek()
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

graph(test4, "Peek() Comparison for Stacks", 4, 1)

def test5(size, trials, stacktype):
    if stacktype == 1:
         my_stack = tStack()
    elif stacktype == 2:
         my_stack = lStack()
    else:
         my_stack = dStack()
         
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        my_stack.size()
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

graph(test5, "Size() Comparison for Stacks", 5, 1)

class tQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

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
        if self.Size == 0:
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
        
    def isEmpty(self):
        if self.values:
             return False
        else:
             return True

    def enqueue(self, item):
        self.values.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.values.popleft()

    def size(self):
        return len(self.values)

def test6(size, trials, queuetype):
    if queuetype == 1:
         my_queue = tQueue()
    elif queuetype == 2:
         my_queue = lQueue()
    else:
         my_queue = dQueue()
     
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        my_queue.isEmpty()
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

graph(test6, "isEmpty() Comparison for Queues", 6, 2)

def test7(size, trials, queuetype):
    if queuetype == 1:
         my_queue = tQueue()
    elif queuetype == 2:
         my_queue = lQueue()
    else:
         my_queue = dQueue()

    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        my_queue.enqueue(5)
        end = time.perf_counter()
        time1 += (end - start)
        my_queue.dequeue()

    avgTime = time1/trials

    return time1

graph(test7, "Enqueue() Comparison for Queues", 7, 2)

def test8(size, trials, queuetype):
    if queuetype == 1:
         my_queue = tQueue()
    elif queuetype == 2:
         my_queue = lQueue()
    else:
         my_queue = dQueue()

    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        my_queue.dequeue()
        end = time.perf_counter()
        time1 += (end - start)
        my_queue.enqueue(5)

    avgTime = time1/trials

    return time1

graph(test8, "Dequeue() Comparison for Queues", 8, 2)

def test9(size, trials, queuetype):
    if queuetype == 1:
         my_queue = tQueue()
    elif queuetype == 2:
         my_queue = lQueue()
    else:
         my_queue = dQueue()

    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        my_queue.size
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

graph(test9, "Size() Comparison for Queues", 9, 2)

def get_ithStack(stack, i, stacktype):
    if i >= stack.size():
        return None
    if stacktype == 1:    
         temp = tStack()
    elif stacktype == 2:
         temp = lStack()
    else:
         temp = dStack()
    for k in range(i):
        temp.push(stack.pop())
    toReturn = stack.peek()
    for k in range(i):
        stack.push(temp.pop())
    return toReturn

def test10(size, trials, stacktype):
    if stacktype == 1:
         my_stack = tStack()
    elif stacktype == 2:
         my_stack = lStack()
    else:
         my_stack = dStack()

    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        get_ithStack(my_stack, size-1, stacktype)
        end =time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

graph(test10, "get_ith() Comparison for Stacks", 10, 1)

def get_ithQueue(queue, i, queuetype):
    if i >= queue.size():
            return None

    if queuetype == 1:    
         temp = tQueue()
    elif queuetype == 2:
         temp = lQueue()
    else:
         temp = dQueue()
         
    for k in range(i):
        temp.enqueue(queue.dequeue())
    toReturn = queue.dequeue()
    temp.enqueue(toReturn)
    for k in range(queue.size()):
        temp.enqueue(queue.dequeue())

    for k in range(temp.size()-1):
        queue.enqueue(temp.dequeue())
            
    return toReturn

def test11(size, trials, queuetype):
    if queuetype == 1:
         my_queue = tQueue()
    elif queuetype == 2:
         my_queue = lQueue()
    else:
         my_queue = dQueue()

    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        get_ithQueue(my_queue, size-1, queuetype)
        end = time.perf_counter()
        time1 += (end - start)

    avgTime = time1/trials

    return time1

graph(test11, "get_ith() Comparison for Queues", 11, 2)

def pushBottom(stack, item):
    temp = dStack()
    for i in range(stack.size()):
        temp.push(stack.pop())
    stack.push(item)
    for i in range(temp.size()):
        stack.push(temp.pop())

def popBottom(stack):
    temp = dStack()
    for i in range(stack.size()-1):
        temp.push(stack.pop())
    stack.pop()
    for i in range(temp.size()):
        stack.push(temp.pop())

def insertFront(queue, item):
    temp = dQueue()
    for i in (range(queue.size())):
        temp.enqueue(queue.dequeue())
    queue.enqueue(item)
    for i in (range(temp.size())):
        queue.enqueue(temp.dequeue())

def removeBack(queue):
    temp = dQueue()
    for i in (range(queue.size() - 1)):
        temp.enqueue(queue.dequeue())
    queue.dequeue()
    for i in (range(temp.size())):
        queue.enqueue(temp.dequeue())

def graph2(fun1, fun2, title, counter):
     # Run test functions for sizes from 1 to 50 and store results for plotting
     plt.figure(counter)
     sizes = range(1, 50, 1)
     x1 = [s for s in sizes]
     x2 = [s for s in sizes]
     y1 = [fun1(s,100) for s in sizes]
     y2 = [fun2(s,100) for s in sizes]  

     # Plot the run times against list lengths
     colors = ['b', 'c']
     alg1 = plt.scatter(x1, y1, color=colors[0])
     alg2 = plt.scatter(x2, y2, color=colors[1])

     # Label axes
     plt.xlabel('size')
     plt.ylabel('run time')

     # Create the legend
     plt.legend((alg1, alg2),('Stack', 'Queue'))

     plt.title(title)

     # Show the plot
     plt.show()

def test12_1(size, trials):
    my_stack = dStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        my_stack.push(5)
        end = time.perf_counter()
        time1 += (end - start)
        my_stack.pop()

    avgTime = time1/trials

    return time1  

def test12_2(size, trials):
    my_queue = dQueue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        insertFront(my_queue, 5)
        end = time.perf_counter()
        time1 += (end - start)
        my_queue.dequeue()

    avgTime = time1/trials

    return time1

graph2(test12_1, test12_2, "Insert Item to Front Comparison for Stacks and Queues", 12)

def test13_1(size, trials):
    my_stack = dStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        my_stack.pop()
        end = time.perf_counter()
        time1 += (end - start)
        my_stack.push(5)

    avgTime = time1/trials

    return time1  

def test13_2(size, trials):
    my_queue = dQueue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        my_queue.dequeue()
        end = time.perf_counter()
        time1 += (end - start)
        my_queue.enqueue(5)

    avgTime = time1/trials

    return time1
        
graph2(test13_1, test13_2, "Remove Item from Front Comparison for Stacks and Queues", 13)

def test14_1(size, trials):
    my_stack = dStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        pushBottom(my_stack, 5)
        end = time.perf_counter()
        time1 += (end - start)
        my_stack.pop()

    avgTime = time1/trials

    return time1      

def test14_2(size, trials):
    my_queue = dQueue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        my_queue.enqueue(5)
        end = time.perf_counter()
        time1 += (end - start)
        my_queue.dequeue()

    avgTime = time1/trials

    return time1

graph2(test14_1, test14_2, "Insert Item to Back Comparison for Stacks and Queues", 14)

def test15_1(size, trials):
    my_stack = dStack()
    time1 = 0

    for i in (range(size)):
        my_stack.push(i)

    for i in range(trials):
        start = time.perf_counter()
        popBottom(my_stack)
        end = time.perf_counter()
        time1 += (end - start)
        my_stack.push(5)

    avgTime = time1/trials

    return time1

def test15_2(size, trials):
    my_queue = dQueue()
    time1 = 0

    for i in (range(size)):
        my_queue.enqueue(i)

    for i in range(trials):
        start = time.perf_counter()
        removeBack(my_queue)
        end = time.perf_counter()
        time1 += (end - start)
        my_queue.enqueue(5)

    avgTime = time1/trials

    return time1

graph2(test15_1, test15_2, "Remove Item from Back Comparison for Stacks and Queues", 15)
