class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] = digits[-1] + 1
        for i in range(len(digits)):
            if digits[-1*(i+1)] == 10:
                if i+1 >= len(digits):
                    digits.insert(0, 1)
                else:
                    digits[-1*(i+2)] += 1
                digits[-1*(i+1)] -= 10
        return digits
