class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = ""
        while (i >= 0 or j >= 0):
            k = int(a[i]) if i >= 0 else 0
            l = int(b[j]) if j >= 0 else 0
            c = k + l + carry
            carry = c // 2
            ans = str(c % 2) + ans
            [i, j] = [i - 1, j - 1]
        return "1" + ans if carry else ans

        # format(int(a,2)+int(b,2), "b")
        
