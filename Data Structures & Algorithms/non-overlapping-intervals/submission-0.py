class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # end が早い順に並べる
        intervals.sort(key=lambda x: x[1])

        remove = 0

        # 最後に残した interval の end
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            # start >= prev_end なら重ならないので残せる
            if start >= prev_end:
                prev_end = end

            # start < prev_end なら重なるので、今の interval を削除する
            else:
                remove += 1

        return remove