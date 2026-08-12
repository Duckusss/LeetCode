class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = int(a) + int(b)
        for i in range(len(str(ans))):
            if int(str(ans)[-1*(i+1)]) >= 2:
                ans += 10**(i+1)
                ans -= 2*(10**i)
        return str(ans)

        # format(int(a,2)+int(b,2), "b")
        
