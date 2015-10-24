# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSameTree(self, p, q):
        if p and q:
            print p
            print q
            print "here"
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q

p=TreeNode(1)
q=TreeNode(2)
print Solution().isSameTree(p,q)