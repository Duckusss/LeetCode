class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        upper = len(nums)
        lower = 0
        while upper > lower:
            mid = (upper-lower)//2 + lower
            if nums[mid] > target:
                upper = mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                return mid
        return -1
        
