class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = []
        while n > 1:
            n = sum([int(digit)**2 for digit in str(n)])
            nums.append(n)
            if len(nums) > len(set(nums)):
                return False
        return True
