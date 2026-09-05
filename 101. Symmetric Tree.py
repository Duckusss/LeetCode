# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetricLR(self, p, q):
        return self.isSymmetricLR(p.left, q.right) and p.val == q.val and self.isSymmetricLR(p.right, q.left) if p and q else p == q
        # this 1 line was a miracle, I'm content for the day
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        step 1: flip right side
        step 2: check if left is right
        step 3 (optional): flip the right side back 


        def isSameTree(self, p, q):
        if p and q:
            return self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right)
        else:
            return p == q
        

        def invertTree(self, root):
            if root:
                self.invertTree(root.left), self.invertTree(root.right) 
                root.left, root.right = root.right, root.left
                return root
            else:
                return None
        

        self.invertTree(root.right)
        A = self.isSameTree(root.right, root.left)
        self.invertTree(root.right)
        return A
        """
        return self.isSymmetricLR(root.left, root.right)
