##Defining the structure for node
class node:
    def __init__(self,data):
        self.data = data
        self.right = None

class singleLinkedList:
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
            
    def linkTraversal(self):
        if self.startnode is None:
            print("linked list is empty")
            return
        else:
            n = self.startnode
            while n is not None:
                print(n.data)
                n = n.right
    
    def reverseLinkedList(self):
        if self.startnode is None:
            print("linked list is empty")
            return
        else:
            prev = None
            next = None
            
            n = self.startnode
            
            while n is not None:
                next = n.right
                n.right = prev
                prev = n
                n = next
            self.startnode = prev

    def countElements(self):
        if self.startnode is None:
            print("list is empty")    
            return
        else:
            n = self.startnode
            count = 0
            while n is not None:
                count += 1
                n = n.right
            return count
        
    def sortLinkList(self):
        n = self.startnode
        
        while n is not None:
            next = n.right
            if n.data == next.data:
                print(next.data)
            n = n.right
                    
s = singleLinkedList()
s.insertelement(5)
s.insertelement(5)
s.insertelement(10)
s.sortLinkList()
##s.reverseLinkedList()
s.linkTraversal()            
##print(s.countElements())