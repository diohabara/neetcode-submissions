class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic= set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0
                    or nc < 0
                    or nr >= ROWS
                    or nc >= COLS
                    or (nr, nc) in visited
                    or heights[nr][nc] < heights[r][c]
                ):
                    continue
                dfs(nr, nc, visited)

        for c in range(COLS):
            dfs(0, c, pacific)           # 上端: Pacific
            dfs(ROWS - 1, c, atlantic)   # 下端: Atlantic

        for r in range(ROWS):
            dfs(r, 0, pacific)           # 左端: Pacific
            dfs(r, COLS - 1, atlantic)   # 右端: Atlantic
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res