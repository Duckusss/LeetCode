class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        d = [0]*(n+1)
        for i in range(1, n+1):
            d[i] = d[i & (i-1)] + 1
        return d
