class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , "Print item ")
                print(n.ref ,  "Print ref ")
                n = n.ref

    def insert_at_end(self, data):
            new_node = Node(data)
            if self.start_node is None:
                self.start_node = new_node
                print("insert", data)
                return
                print("post return ", data)
                
            n = self.start_node
            print("checking logic", n.item )
            while n.ref is not None:
                print("inserting")
                n= n.ref
                print("data 1234", n.item)
            n.ref = new_node
            print("printing", data)
                   
new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
print("insert 5 completed")
new_linked_list.insert_at_end(10)
print("insert 10 completed")
new_linked_list.insert_at_end(15)        
print("insert 15 completed")
new_linked_list.traverse_list()