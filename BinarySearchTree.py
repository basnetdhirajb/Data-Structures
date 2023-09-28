#Implementing a binary search tree without recursion
COUNT = [10]

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        
    def print2DUtil(self,root,space):
        # Base case
        if (root == None):
            return
    
        # Increase distance between levels
        space += COUNT[0]
    
        # Process right child first
        self.print2DUtil(root.right, space)
    
        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root.data)
    
        # Process left child
        self.print2DUtil(root.left, space)
    
    
    def insert(self, value):
        node = Node(value)
        #If there is no root node, or the tree is empty
        if self.root is None:
            self.root = node
            return

        #If there is a root in the tree already
        currentNode = self.root     
        
        while currentNode is not None:
            if node.data <= currentNode.data:
                if currentNode.left is None:
                    currentNode.left = node
                    return
                else:
                    currentNode=currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = node
                    return
                else:
                    currentNode=currentNode.right
        return self

    def lookup(self,value):
        node = Node(value)
        currentNode = self.root
        
        if not currentNode:
            return "Empty Tree"
        
        while currentNode is not None:
            if node.data < currentNode.data:
                currentNode = currentNode.left
            elif node.data > currentNode.data:
                currentNode = currentNode.right
            else:
                return "Found"
        return "Not Found"
            

bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(7)
bst.insert(14)
bst.print2DUtil(bst.root,0)
print(bst.lookup(7))