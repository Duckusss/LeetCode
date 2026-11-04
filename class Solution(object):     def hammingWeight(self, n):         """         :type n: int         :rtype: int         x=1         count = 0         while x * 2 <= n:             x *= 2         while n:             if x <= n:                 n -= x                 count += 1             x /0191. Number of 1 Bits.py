class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        x=1
        count = 0
        while x * 2 <= n:
            x *= 2
        while n:
            if x <= n:
                n -= x
                count += 1
            x //= 2
        return count
        """
        return sum(map(int, bin(n)[2:]))
