from bisect import bisect_left

class Solution:
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        ps=[0]*(n+1)
        for i,x in enumerate(nums):
            ps[i+1]=ps[i]+x
        res=n+1
        for i in range(n):
            # ps[j]-ps[i]がtarget以上になる最小jを二分探索で探す
            j=bisect_left(ps,ps[i]+target)
            if j<=n:
                res = min(res, j-i)
                if res<=1:
                    return 1
        if n<res:
            return 0
        return res