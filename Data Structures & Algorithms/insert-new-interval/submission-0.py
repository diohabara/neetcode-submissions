class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        res = []
        i = 0
        n = len(intervals)

        new_start, new_end = newInterval

        # 1. newInterval より左にある interval を全部追加
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1

        # 2. overlap する interval を全部 merge
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        # merge された newInterval を追加
        res.append([new_start, new_end])

        # 3. newInterval より右にある interval を全部追加
        while i < n:
            res.append(intervals[i])
            i += 1

        return res