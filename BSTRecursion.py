class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
        
    def insert(self,root,value):
        node = Node(value)
        if root is None:
            return node
        
        if value < root.value:
            root.left = self.insert(root.left,value)
        else:
            root.right = self.insert(root.right, value)
        
        return root

    def lookup(self, root, value):
        if root is None:
            return None
        if root.value == value:
            return root
        if value < root.value:
            return self.lookup(root.left,value)
        else:
            return self.lookup(root.right, value)
        
        

bst = Node(4)
bst = bst.insert(bst,2)
bst = bst.insert(bst,7)
bst = bst.insert(bst,1)
bst = bst.insert(bst,3)

print(bst.left.right.value)

print(bst.lookup(bst,0).value)