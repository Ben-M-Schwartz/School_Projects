from collections import deque

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

    def pushBottom(self, item):
        temp = Stack()
        for i in range(self.size()):
            temp.push(self.pop())
        self.push(item)
        for i in range(temp.size()):
            self.push(temp.pop())

    def popBottom(self):
        temp = Stack()
        for i in range(self.size()-1):
            temp.push(self.pop())
        toReturn = self.pop()
        for i in range(temp.size()):
            self.push(temp.pop())

        return toReturn

myStack = Stack()
myStack.push(0)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.pushBottom(10)
print(myStack.size())
print(myStack.get_ith(0))
print(myStack.get_ith(1))
print(myStack.get_ith(2))
print(myStack.get_ith(3))
print(myStack.get_ith(4))
print(myStack.get_ith(5))
print(myStack.popBottom())
