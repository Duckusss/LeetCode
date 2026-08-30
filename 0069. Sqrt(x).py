class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # i = 1
        # if x < 2:
        #     return x
        # while i * i <= x:
        #     i *= 2
        # i /= 2
        # if i * i == x:
        #     return i
        # while i * i <= x:
        #     i += 1000
        # while i * i > x:
        #     i -= 100
        # while i * i <= x:
        #     i += 10
        # while i * i > x:
        #     i -= 1
        # return i
        h = x
        l = 0
        c = 1
        while h-l > 1:
            c = l+(h-l+1)//2
            if c*c > x:
                h = c
            else:
                l = c
        return l if x > 1 else x
