# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        target = targetSum - root.val

        if not root.left and not root.right:
            return not target
        
        if self.hasPathSum(root.left, target):
            return True
        else:
            return self.hasPathSum(root.right, target)
        
        """
        left = self.hasPathSum(root.left, target)
        right = self.hasPathSum(root.right, target)
        return left or right
        "return target == 0 or left or right"
        # I'm so bad at coding
        """
