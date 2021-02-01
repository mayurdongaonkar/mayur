class CNode(object):
    def  __init__(self):
        self.data  = None
        self.left  = None
        self.right = None

class solutions:
    a = 10
    def isSame(self, T1:CNode, T2:CNode):
        if T1.data == T2.data:
            return True
        else:
            return False

T1 = CNode()
T1.data = 10
print(T1.data)

T2 = CNode()
T2.data = 20
print(T2.data)

s1 = solutions()
print(s1.isSame(T1,T2))

print(s1.a)