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
        self.size = 0
      
    def isempty(self): 
        if self.top == None: 
            return True
        else: 
            return False
       
    def push(self,data): 
          
        if self.top == None: 
            self.top=Node(data)
            self.size++
              
        else: 
            newnode = Node(data) 
            newnode.setNext(self.top) 
            self.top = newnode
            self.size++
       
    def pop(self): 
          
        if self.isempty(): 
            return None
              
        else:  
            poppednode = self.top
            self.top = self.top.getNext()
            poppednode.setNext(None)
            self.size--
            return poppednode.data
        
    def peek(self): 
          
        if self.isempty(): 
            return None
              
        else: 
            return self.top.getData()

    def size(self):
        return self.size
