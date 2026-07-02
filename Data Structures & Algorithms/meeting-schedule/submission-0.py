"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # start time でソートする
        intervals.sort(key=lambda interval: interval.start)

        # 隣り合う会議だけ確認すればよい
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            # curr が prev の終了前に始まるなら overlap
            if curr.start < prev.end:
                return False

        return True