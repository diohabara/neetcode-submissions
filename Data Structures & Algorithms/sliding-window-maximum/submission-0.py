class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 直感: 最大になり得る候補だけ持てばいい
        # 新しい値nums[i]が大きいなら、それ以下の過去候補は将来最大になれないので捨ててよい
        # dequeには「値が単調減少になるように」indexを保持する
        # 時間計算量: O(n) (各要素は高々1回appendされ高々1回popされる)
        # 空間計算量: O(k)
        dq = deque()
        res = []
        for i in range(len(nums)):
            # 窓の左端より外のindexを捨てる
            while dq and dq[0] <= i - k:
                dq.popleft()
            # 単調減少を維持: 後ろが新要素以下なら、その後ろは不要
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            # iがk-1以上になったら1つ目の窓が完成
            if k - 1 <= i:
                res.append(nums[dq[0]])
        return res
