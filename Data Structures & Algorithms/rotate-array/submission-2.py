class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return
        def rev(l, r):
            # nums[l:r+1]を両端からswapして反転する
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        rev(0, n - 1) # 全体
        rev(0, k - 1) # 先頭k部分
        rev(k, n - 1) # 残り