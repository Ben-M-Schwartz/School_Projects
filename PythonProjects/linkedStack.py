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
      
class Stack:  
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

    def get_ith(self, i):
        if i >= self.size():
            return None
        
        temp = Stack()
        for k in range(i):
            temp.push(self.pop())
        toReturn = self.peek()
        for k in range(i):
            self.push(temp.pop())
        return toReturn

myStack = Stack()
myStack.push(0)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
print(myStack.size())
print(myStack.get_ith(0))
print(myStack.get_ith(1))
print(myStack.get_ith(2))
print(myStack.get_ith(3))
print(myStack.get_ith(4))
print(myStack.get_ith(5))
print(myStack.get_ith(2))
