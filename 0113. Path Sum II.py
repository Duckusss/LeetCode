# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def merge(self, val, path):
        if any(isinstance(element, list) for element in path) and path:
                for i in range(len(path)):
                    path[i] = [val] + (path[i] if isinstance(path[i], list) else [path[i]])
        else:
            path = [val] + path
        return path
    

    def findPaths(self, root, targetSum):
        if not root: 
            return []

        target = targetSum - root.val
        left, right = self.findPaths(root.left, target), self.findPaths(root.right, target)

        if not root.left and not root.right:
            return [] if target else [root.val]
        
        if not left and not right:
            return []
        
        elif not left or not right:
            return self.merge(root.val, left + right)
        
        else:
            left = self.merge(root.val, left)
            right = self.merge(root.val, right)
            if any(isinstance(element, list) for element in left) and any(isinstance(element, list) for element in right):
                return left + right
            elif any(isinstance(element, list) for element in left):
                return left + [right]
            elif any(isinstance(element, list) for element in right):
                return [left] + right
            else:
                return [left, right]
    

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths = self.findPaths(root, targetSum)
        return paths if any(isinstance(element, list) for element in paths) or not paths else [paths]
