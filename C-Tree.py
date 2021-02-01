# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

T1 = TreeNode([3,4,5,1,2])
T2 = TreeNode([4,1,2])

print(T1.val)
print(T1.left)
print(T1.right)

print(T2.val)
print(T2.left)
print(T2.right)

class Solution:
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: 
            return False
        if self.isSameTree(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

Sol = Solution()
print(Sol.isSameTree(T1,T2))