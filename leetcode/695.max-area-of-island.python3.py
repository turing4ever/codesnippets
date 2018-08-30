class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def ones(i, j):
            if 0<=i<m and 0<=j<n and grid[i][j]:
                grid[i][j] = 0 
                return 1 +  ones(i, j-1) + ones(i, j+1) + ones(i-1, j) + ones(i+1, j)
            return 0
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxi = max(maxi, ones(i, j))
        return maxi
