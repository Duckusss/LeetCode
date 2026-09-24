class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = [1]
        for i in range(rowIndex):
            output = ([1]+[output[element]+output[element+1] for element in range(len(output)-1)]+[1])
        return output
        
