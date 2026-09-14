# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        1. find middle value
        2. recursive function for left and right side
        3. return Treenode(value, left, right)
        """
        # start = 0
        end = len(nums)
        if end:
            # mid = start + (start + end)//2
            mid = end//2  # oohhhhh. So we don't need the start because the original array is already cut in half.
            # mid = mid if mid >= 0 else 0
            return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))
        else: 
            return None
