from copy import deepcopy

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = deepcopy(M) 
        for i in range(len(M)):
            new_row = []
            for j in range(len(M[i])):
                running_sum = 0
                cnt = 0
                rows = [i-1, i, i+1]
                cols = [j-1, j, j+1]
                for r,c in [(r, c) for r in rows for c in cols]:
                    if r >= 0 and r <= len(M)-1 and c >=0 and c<=len(M[r])-1:
                        running_sum += M[r][c]
                        cnt += 1
                ret[i][j] = running_sum//cnt
        return ret
