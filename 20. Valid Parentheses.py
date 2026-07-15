class Solution(object):
    def isValid(self, s):
        stack = []
        map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            elif not stack or stack.pop() != map[i]:
                return False
        return not stack
      
