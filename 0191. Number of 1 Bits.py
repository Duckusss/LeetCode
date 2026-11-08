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
        
        return sum(map(int, bin(n)[2:]))

        total = 0
        while n > 0:
            n = n & (n-1)
            total += 1
        return total
        """

        return self.hammingWeight(n & (n-1)) + 1 if n & (n-1) > 0 else 1
