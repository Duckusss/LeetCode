class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[-1*(i+1)] != " ":
                for j in range(len(s)-i):
                    if s[-1*(j+i+1)] == " ":
                        return j
                return len(s)-i
        
        # words = s.split()
        # return len(words[-1])
