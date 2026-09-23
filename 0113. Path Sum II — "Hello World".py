# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
paths = []
class Solution(object):
    def findPath(self, root, targetSum, curr_path):
        global paths
        if not root:
            return "Hello World"
        target = targetSum - root.val
        if not root.left and not root.right and target == 0:
            paths += [curr_path + [root.val]]
        self.findPath(root.left, target, curr_path + [root.val])
        self.findPath(root.right, target, curr_path + [root.val])
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        global paths
        paths = []
        a = self.findPath(root, targetSum, [])
        return paths
