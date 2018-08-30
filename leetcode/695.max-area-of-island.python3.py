class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def ones(i, j):
            if grid[i][j] == 1:
                grid[i][j] = 0 
                yield i,j
                if j-1 >= 0:
                    yield from ones(i, j-1)
                if j+1 < n:
                    yield from ones(i, j+1)
                if i-1 >= 0 :
                    yield from ones(i-1, j)
                if i+1 < m: 
                    yield from ones(i+1, j)

        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxi = max(maxi, sum(1 for i in ones(i, j)))
        return maxi
