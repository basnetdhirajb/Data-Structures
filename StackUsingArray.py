class Stack:
    def __init__(self) -> None:
        self.data = []
        
        
    def __repr__(self) -> str:
        return "<-".join(self.data)
    
    def push(self,value):
        self.data.append(value)
        
    def peek(self):
        return self.data[len(self.data)-1]

    def pop(self):
        self.data.pop()

myStack = Stack()
myStack.push('discord')
myStack.push('udemy')
myStack.push('google')
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)