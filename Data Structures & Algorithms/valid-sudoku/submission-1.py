class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        row, col = len(board), len(board[0])
        r_set = defaultdict(list)
        c_set = defaultdict(list)
        s_set = defaultdict(list)
        for r in range(row):
            for c in range(col):
                cur = board[r][c]
                if cur == ".":
                    continue
                sub_r, sub_c = r // 3, c // 3
                if cur in r_set[r]:
                    return False
                if cur in c_set[c]:
                    return False
                if cur in s_set[(sub_r, sub_c)]:
                    return False
                r_set[r].append(cur)
                c_set[c].append(cur)
                s_set[(sub_r, sub_c)].append(cur)
        return True
