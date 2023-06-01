class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

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
