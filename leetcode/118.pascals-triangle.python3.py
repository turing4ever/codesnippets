class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for level in range(numRows):
            if level > 0:
                n = [result[level-1][i-1]+ result[level-1][i] if i>0 and i<level else 1 for i in range(level+1)]
                result.append(n)
            else:
                result.append([1])
        return result
                 
        
