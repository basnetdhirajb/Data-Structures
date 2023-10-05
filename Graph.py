class Graph:
    def __init__(self) -> None:
        self.numberOfNodes = 0
        self.adjacentList={}
    
    def addVertex(self, node):
        self.numberOfNodes+=1
        self.adjacentList[node] = []
    
    def addEdge(self,node1,node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
    
    def showConnection(self):
        for vertex, neighbors in self.adjacentList.items():
            print(vertex, end = '-->')
            print(' '.join(neighbors))
        
myGraph = Graph()

myGraph.addVertex('5')

myGraph.addVertex('8')

myGraph.addVertex('9')

myGraph.addVertex('10')

myGraph.addEdge('5', '8')

myGraph.addEdge('5', '9')

myGraph.addEdge('10', '8')

myGraph.showConnection()