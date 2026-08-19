class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        if x < 2:
            return x
        while i * i <= x:
            i *= 2
        i /= 2
        if i * i == x:
            return i
        while i * i <= x:
            i += 1000
        while i * i > x:
            i -= 100
        while i * i <= x:
            i += 10
        while i * i > x:
            i -= 1
        return i
