class Solution:
    def findMin(self, nums: list[int]) -> int:
        # 直感: nums[-1]を基準にすると「右区間(小さい側)」はnums[i]<=nums[-1]が成り立つ
        # P(i)=nums[i]<=nums[-1]はFalse...False, True...Trueの単調になる(ユニーク前提)
        # めぐる式で「最初のTrue」を探せば最小値の位置になる
        # 時間計算量: O(log n)
        # 空間計算量: O(1)
        n=len(nums)
        x=nums[n-1]
        def is_ok(i: int) -> bool:
            # iが右区間側ならTrue(=最小値候補側)
            return nums[i]<=x
        ng=-1
        ok=n-1
        while 1<ok-ng:
            mid=(ok+ng)//2
            if is_ok(mid):
                ok=mid
            else:
                ng=mid
        return nums[ok]