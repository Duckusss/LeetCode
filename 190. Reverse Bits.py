class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(("0"*(32-len(bin(n)[2:])) + bin(n)[2:])[::-1], 2)
