from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self._dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self._dict[key]
        idx = bisect_right(arr, (timestamp, chr(127))) - 1
        if idx < 0:
            return ""
        return arr[idx][1]