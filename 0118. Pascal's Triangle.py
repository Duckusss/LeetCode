class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = [[1]]
        for i in range(numRows-1):
            output.append([1]+[output[i][element]+output[i][element+1] for element in range(len(output[i])-1)]+[1])
        return output
        
