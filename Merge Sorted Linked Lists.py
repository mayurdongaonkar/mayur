class ListNode:
    def Node(self,val = 0,next = None):
        self.val = val
        self.next = next
        
def mergeTwoLists(l1,l2):
    start = end = 0
    
    while l1 and l2:
        if l1.val < l2.val:
            end.next = l1
            l1 = l1.next
        else:
            end.next = l2
            l2 = l2.next 
        
        end = end.next
        
        if l1: end.next = l1
        if l2: end.next = l2
        
        return start.next


L1 = ListNode()
L2 = ListNode()

l1 = L1.Node(1,L1.Node(2,L1.Node(3)))
l2 = L1.Node(1,L1.Node(2,L1.Node(3)))

print(mergeTwoLists(l1,l2))