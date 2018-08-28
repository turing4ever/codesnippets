class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        def avg(M, i, j):
            running_sum = 0
            cnt = 0
            rows = [i-1, i, i+1]
            cols = [j-1, j, j+1]
            for r,c in [(r, c) for r in rows for c in cols]:
                if r >= 0 and r <= n-1 and c >=0 and c<=len(M[r])-1:
                    running_sum += M[r][c]
                    cnt += 1
            return int(running_sum/cnt)
        ret = []
        for i in range(n):
            ret.append([avg(M, i, j) for j in range(len(M[i]))])
        return ret
