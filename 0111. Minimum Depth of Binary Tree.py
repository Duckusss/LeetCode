# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            elif not root.left:
                return self.minDepth(root.right) + 1
            elif not root.right:
                return self.minDepth(root.left) + 1
        else:
            return 0
