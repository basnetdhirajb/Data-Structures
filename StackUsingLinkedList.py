class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
        
    def __iter__(self):
        node = self.top
        while node is not None:
            yield node
            node = node.next
        
    def __repr__(self) -> str:
        node = self.top
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)
        
    def isEmpty(self):
        return self.top==None
    
    def peek(self):
        return self.top.data
        
    def push(self,value):
        node = Node(value)
        if self.isEmpty():
            self.top = node
            self.bottom = node
            node.next = None
        else:
            node.next = self.top
            self.top = node
        self.length+=1
            
    def pop(self):
        if not self.isEmpty():
            newHead = self.top.next
            self.top = newHead
            self.length-=1
            return
        return 'Empty Stack'
    
myStack = Stack()
myStack.push('discord')
myStack.push('udemy')
myStack.push('google')
print(myStack)
myStack.pop()
print(myStack)
myStack.pop()
print(myStack)



