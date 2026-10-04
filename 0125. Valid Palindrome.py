class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 3.
        return [new == new[::-1] for new in [''.join(char.lower() for char in s if char.isalnum())]][0]

        """
        # 1.
        new = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new += s[i].lower()
        return new[i] != new[-i-1]
        # 2.
        new = ''.join([s[i].lower() for i in range(len(s)) if s[i].isalnum()])
        new == new[::-1]
        """
        
