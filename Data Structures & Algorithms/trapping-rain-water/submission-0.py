class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lefts, rights = [0] * n, [0] * n # left, right highest
        lefts[0] = height[0]
        rights[-1] = height[-1]
        for i in range(1, n):
            lefts[i] = max(height[i], lefts[i-1])
        for i in range(1, n):
            rights[n-1-i] = max(height[n-1-i], rights[n-i])
        area = 0
        for i in range(0, n-1):
            min_bar = min(lefts[i], rights[i])
            area += max(0, min_bar - height[i])
        return area