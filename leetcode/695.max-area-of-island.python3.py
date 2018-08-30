class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def ones(grid, i, j):
            if grid[i][j] == 1:
                grid[i][j] = 0 
                yield i,j
                if j-1 >= 0:
                    yield from ones(grid, i, j-1)
                if j+1 < len(grid[i]):
                    yield from ones(grid, i, j+1)
                if i-1 >= 0 :
                    yield from ones(grid, i-1, j)
                if i+1 < len(grid): 
                    yield from ones(grid, i+1, j)

        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxi = max(maxi, len(list(ones(grid, i, j))))
        return maxi
