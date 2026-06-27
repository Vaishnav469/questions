class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numrows, numcols = len(grid),len(grid[0])
        numlands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= numrows or c >= numcols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(numrows):
            for c in range(numcols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    numlands += 1

        return numlands
        