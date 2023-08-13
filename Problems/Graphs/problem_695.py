class Solution:
    def Dfs(self, row, column, grid):
        if str(row)+":"+str(column) in self.visited:
            return
        if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]):
            return
        if grid[row][column] == 0:
            return
        self.visited.add(str(row)+":"+str(column))
        self.area += grid[row][column]
        a1 = Solution.Dfs(self, row-1, column, grid)
        a2 = Solution.Dfs(self, row, column-1, grid)
        a3 = Solution.Dfs(self, row+1, column, grid)
        a4 = Solution.Dfs(self, row, column+1, grid)

    def maxAreaOfIsland(self, grid) -> int:
        self.visited = set()
        self.area = 0
        maxArea = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1 and str(i)+":"+str(j) not in self.visited:
                    Solution.Dfs(self, i, j, grid)
                    maxArea = max(self.area, maxArea)
                    self.area = 0
        return maxArea


obj = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

assert obj.maxAreaOfIsland(grid=grid) == 6, "Incorrect Max Answer"
