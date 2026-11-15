class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

        return (len(nums)*(len(nums)+1)/2 - sum(nums)
        """
        a = 0
        for num in range(len(nums)):
            # x^a^a = x
            a = a^(num + 1)^nums[num]
        return a
