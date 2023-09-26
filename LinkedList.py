class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0
    self.tail = None
    
  def __repr__(self):
          node = self.head
          nodes = []
          while node is not None:
              nodes.append(node.data)
              node = node.next
          nodes.append("None")
          return " -> ".join(nodes)

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  def append(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
      self.tail = node
      self.length+=1
      return

    self.tail.next = node
    self.tail = node
    self.length+=1

  def prepend(self,value):
     node = Node(value)
     node.next = self.head
     self.head = node
     self.length+=1
    
  def insert(self,value,targetIndex):
    node = Node(value)
    index = 0

    if targetIndex > self.length -1:
        self.append(value=value)
        return
    
    if targetIndex == 0:
       self.prepend(value=value)
       return
    
    previous_node = self.head
    for currentNode in self:
        if index == targetIndex:
            node.next=currentNode
            previous_node.next=node
            self.length+=1
            return
        previous_node=currentNode
        index+=1

  def remove(self,target):
      index = 0
      
      if target > self.length-1:
          print('Target greate than length')
          return
      
      if target == 0:
          self.head = self.head.next
          Node(self.head).prev = None
          return
       
      previous_node = self.head
      for currentNode in self:
          if index == target:
              previous_node.next=currentNode.next
              currentNode.next=None
              if target == self.length-1:
                  self.tail = previous_node
              self.length-=1
              return
          previous_node = currentNode
          index+=1
              
  def reverse(self):
    prev = None
    curr = self.head
    self.tail = self.head
    while curr is not None:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    self.head = prev
    return self
    
    
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

  def __repr__(self):
        return self.data
      
myList = LinkedList()
myList.append('A')
myList.append('B')
myList.append('C')
myList.append('D')
print(myList.reverse())