class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
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
        return "->".join(nodes)
            
    def isEmpty(self):
        return self.top == None
    
    def peek(self):
        if self.top:
            return self.top.data
    
    def enqueue(self,value):
        node = Node(value)
        if self.isEmpty():
            self.top = node
            self.bottom = node
        else:
            self.bottom.next = node
            self.bottom = node
        self.length+=1
        
    def dequeue(self):
        if not self.isEmpty():
            self.top = self.top.next
            self.length-=1
        return 'Empty Queue'

