## Create structure for Node.
class Node:
    def __init__(self,data):
        self.item = data
        self.right = None
        
## Create linked list framework
class singlyLinkedList:
    def __init__(self):
        self.startingNode = None
    
    def insertSLL(self,data):
        newnode = Node(data)
        
        if self.startingNode is None:
            self.startingNode = newnode
            return
        else:
            n = self.startingNode
            while n.right is not None:
                n = n.right
            n.right = newnode
            
    def traverse_list(self):
        if self.startingNode is None:
            print("List has no element")
            return
        else:
            n = self.startingNode
            while n is not None:
                print("Print item ", n.item)
                print("Print ref " , n.right)
                n = n.right
            
L1 = singlyLinkedList()
L1.insertSLL(5)
L1.insertSLL(10)
L1.traverse_list()