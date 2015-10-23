# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0     

root=TreeNode("Root")
left=TreeNode("Left")
right=TreeNode("Right")
left_left=TreeNode("Left_L2")
right_right=TreeNode("Right_L2")
root.left=left
root.right=right
left.left=left_left
right.right=right_right
root.left.left.left=TreeNode("Left_L3")
root.right.right.right=TreeNode("Right_L3")

print root.val
print Solution().maxDepth(root)		
print root.left.left.val
#print Left.val
#print Solution().maxDepth(Left)
#print Solution().maxDepth(Right)