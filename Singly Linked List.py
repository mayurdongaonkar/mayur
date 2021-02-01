class ListNode():
    def __init__(self):
         self.val = None
         self.next = None

T1 = ListNode()
T1.val = 1
print(T1.val)
    
T2 = ListNode()
T2.val = 2
print(T2.val)

T3 = ListNode()
T3.val = 3
print(T3.val)

T1.next = id(T2)
T2.next = id(T3)
T3.next = None

import ctypes
print(T1.next)
print(ctypes.cast(T1.next, ctypes.py_object).value)

