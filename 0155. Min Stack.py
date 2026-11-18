class MinStack(object):

    def __init__(self):
        self.stack = []
        self.sorted_stack = []
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        bisect.insort(self.sorted_stack, value)

    def pop(self):
        """
        :rtype: None
        """
        self.sorted_stack.remove(self.stack[-1])
        self.stack = self.stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.sorted_stack[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
