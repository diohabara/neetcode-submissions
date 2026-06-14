class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.cum_sum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(1, len(matrix) + 1):
            for c in range(1, len(matrix[0]) + 1):
                self.cum_sum[r][c] = matrix[r-1][c-1] + self.cum_sum[r-1][c] + self.cum_sum[r][c-1] - self.cum_sum[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.cum_sum[row2][col2] - self.cum_sum[row1-1][col2] - self.cum_sum[row2][col1-1] + self.cum_sum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)