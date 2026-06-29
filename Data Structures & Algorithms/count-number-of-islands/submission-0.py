class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
            if (r < 0
                or c < 0
                or ROWS <= r
                or COLS <= c):
                return
            if grid[r][c] == '1':
                grid[r][c] = '#'
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    cnt += 1
                    dfs(r, c)
        return cnt
