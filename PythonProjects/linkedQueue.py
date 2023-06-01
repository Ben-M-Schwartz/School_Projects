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
        
class Queue: 
      
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
        
