#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 1st solution. (Intuition idea)
        if ((p.val == root.val) or (q.val==root.val)):
            return root
        elif (p.val<root.val) and (q.val<root.val):
            self.lowestCommonAncestor(root.left,p,q)
        elif (p.val>root.val) and (q.val>root.val):
            self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
root = TreeNode()
L1F=TreeNode()
L1R=TreeNode()
L2LL=TreeNode()
L2LR=TreeNode()
L3LLL=TreeNode()
Solution().lowestCommancestor(5,1,4)