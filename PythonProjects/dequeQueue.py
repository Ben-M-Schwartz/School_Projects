from collections import deque

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

    def get_ith(self, i):
        if i >= self.size():
            return None
        
        temp = Queue()
        for k in range(i):
            temp.enqueue(self.dequeue())
        toReturn = self.dequeue()
        temp.enqueue(toReturn)
        for k in range(self.size()):
            temp.enqueue(self.dequeue())

        for k in range(temp.size()):
            self.enqueue(temp.dequeue())
            
        return toReturn

    def insertBack(self, item):
        temp = Queue()
        for i in (self.size()):
            temp.enqueue(self.dequeue())
        self.enqueue(item)
        for i in (temp.size()):
            self.enqueue(temp.dequeue())

    def removeBack(self, item):
        temp = Queue()
        for i in (self.size() - 1):
            temp.enqueue(self.dequeue())
        toReturn = self.dequeue()
        for i in (temp.size()):
            self.enqueue(temp.dequeue())

myQueue = Queue()
myQueue.enqueue(0)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
print(myQueue.size())
print(myQueue.get_ith(0))
print(myQueue.get_ith(1))
print(myQueue.get_ith(2))
print(myQueue.get_ith(3))
print(myQueue.get_ith(4))
print(myQueue.get_ith(5))
print(myQueue.get_ith(2))
