class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1] * (n+1)
        for i in range(2,(n+1)):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[-1]
        
