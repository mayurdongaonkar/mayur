class node:
    def __init__(self,data):
        self.item = data
        self.right = None

class linkedlist:
    def __init__(self):
        self.startnode = None
    
    def insertelement(self,data):
        newnode = node(data)
        
        if self.startnode is None:
            self.startnode = newnode
            return
        else:
            n = self.startnode
            while n.right is not None:
                n = n.right    
            n.right = newnode
    
    def linkedlistTraverse(self):
        if self.startnode is None:
            print("Linked list is empty.....")
            return
        else:
            n = self.startnode
            while n is not None:
                print(n.item)
                n = n.right
    
    def linkedlistReverse(self):
        n = self.startnode
        
        if self.startnode is None:
            print("Linked list is empty.OOOOO")
            return
        else:
            prev = None
            
            while n is not None:
                next = n.right 
                n.right = prev
                prev = n
                n = next
            self.startnode = prev
    
    def countElements(self):
        count = 0
        if self.startnode is None:
            print("Linked list is empty")
            return
        else:
            n = self.startnode
            while n is not None:
                count = count + 1
            return count
                                          

LL = linkedlist()
LL.insertelement(5)
LL.insertelement(10)
LL.insertelement(15)
LL.linkedlistTraverse()
LL.linkedlistReverse()
LL.linkedlistTraverse()
LL.countElements()