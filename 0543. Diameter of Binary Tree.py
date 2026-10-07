# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_diameter = 0
class Solution(object):
    def diameter(self, root):
        global max_diameter
        if root:
            left, right = self.diameter(root.left), self.diameter(root.right)
            if left + right > max_diameter:
                max_diameter = left + right
            return max(left, right) + 1
        else:
            return 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        global max_diameter
        max_diameter = 0
        if root:
            left, right = self.diameter(root.left), self.diameter(root.right)
            if left + right > max_diameter:
                max_diameter = left + right
            return max_diameter
        else:
            return 0
        
