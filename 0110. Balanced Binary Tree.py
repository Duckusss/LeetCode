# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root:
            if not self.isBalanced(root.left) or not self.isBalanced(root.right):
                return False
            if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1:
                return True
            else:
                return False
        else:
            return True
# omg how do I do stacks
