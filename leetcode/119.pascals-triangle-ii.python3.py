class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tmp = [[0]*(rowIndex+1)] + [[0]*(rowIndex+1)]
        for row in range(rowIndex+1):
            if row == 0:
                tmp[0][0] = 1
            else:
                i = row % 2
                last = (row-1) % 2
                for col in range(row+1):
                    if col > 0 and col < row:
                        tmp[i][col] = tmp[last][col-1] + tmp[last][col]
                    else:
                        tmp[i][col] = 1
        return tmp[rowIndex%2][:rowIndex+1]

        
