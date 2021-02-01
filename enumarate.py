l1 = [1,2,3,4,5,6,7]

for k,v in enumerate(l1):
    print(k,v)
    print(type(k),type(v))
    
print(float('inf'))    

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            
        return new_head```