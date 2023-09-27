class Stack:
    def __init__(self) -> None:
        self.data = []
        
    def __repr__(self) -> str:
        return "<-".join(self.data)
    
    def push(self,value):
        self.data.append(value)
        
    def peek(self):
        if len(self.data) > 0:
            return self.data[len(self.data)-1]

    def pop(self):
        if len(self.data) > 0:
            self.data.pop()