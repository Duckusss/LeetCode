class Solution(object):
    def longestCommonPrefix(self, strs):
        LCP = 0
        for i in range(min(len(word) for word in strs)):
            if len(set(word[i] for word in strs)) == 1:
                LCP += 1
            else:
                break
        return strs[0][0:LCP] if LCP else ""
