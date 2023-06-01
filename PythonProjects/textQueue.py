class Queue:
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
