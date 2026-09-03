class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root:
            self.invertTree(root.left), self.invertTree(root.right) 
            root.left, root.right = root.right, root.left
            return root
        else:
            return None
