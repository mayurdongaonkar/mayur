##Create a frame for Node
class Node:
    def __init__(self,data):
        self.item = data
        self.right = None
        
##Create linked list        
class linkedlist:
    def __init__(self):
        self.startnode = None
        
    
    def insert_linkedlist(self,data):
        newNode = Node(data)
        
        if self.startnode is None:
            self.startnode = newNode
            return
        else:
            n = self.startnode
            
            while n.right is not None:
                n = n.right
            
            n.right = newNode
                        
    def traverse_linklist(self):
        if self.startnode is None:
            print("empty linked list")
            return
        else:
            n = self.startnode
            while n is not None:
                print(n.item)
                n = n.right
                
    def reverse_linkedlist(self):
        prev = None
        n = self.startnode
        while n is not None:
            next = n.right
            n.right = prev
            prev = n
            n = next
        self.startnode = prev
                    
L1 = linkedlist()
L1.insert_linkedlist(5)
L1.insert_linkedlist(10)
L1.insert_linkedlist(15)
L1.reverse_linkedlist()
L1.traverse_linklist()