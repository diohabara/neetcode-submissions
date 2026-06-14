class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        # row
        for r in range(m):
            visited = set()
            for c in range(n):
                if board[r][c] == '.':
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])
        # column
        for c in range(n):
            visited = set()
            for r in range(m):
                if board[r][c] == '.':
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])
        # sub
        for r in range(0, m, 3):
            for c in range(0, n, 3):
                visited = set()
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] == '.':
                            continue
                        if board[r+i][c+j] in visited:
                            return False
                        visited.add(board[r+i][c+j])
        return True