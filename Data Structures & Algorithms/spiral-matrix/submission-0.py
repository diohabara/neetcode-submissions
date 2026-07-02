class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. 上の行を左から右へ
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. 右の列を上から下へ
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. 下の行を右から左へ
            # top <= bottom を確認しないと、同じ行を二重に読むことがある
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. 左の列を下から上へ
            # left <= right を確認しないと、同じ列を二重に読むことがある
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res