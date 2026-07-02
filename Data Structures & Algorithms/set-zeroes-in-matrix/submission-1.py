from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # 1行目に 0 があるか
        first_row_zero = False
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # 1列目に 0 があるか
        first_col_zero = False
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # 1行目・1列目を marker として使う
        # matrix[r][c] == 0 なら、
        # r行目とc列目を後で0にする印をつける
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # marker に基づいて、内側部分を0にする
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 最初の1行目に0があったなら、1行目全体を0にする
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0

        # 最初の1列目に0があったなら、1列目全体を0にする
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0