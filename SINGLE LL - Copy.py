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
                return
            n = self.start_node
            while n.ref is not None:
                n= n.ref
            n.ref = new_node
                   
new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)        
new_linked_list.traverse_list()