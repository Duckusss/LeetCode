# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) if p and q else p == q
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) if root else False
        
