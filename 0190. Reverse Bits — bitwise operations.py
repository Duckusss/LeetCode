class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        for i in range(31):
            if (n & (1 << i)):
                output |=  1
            output <<= 1
        return output
