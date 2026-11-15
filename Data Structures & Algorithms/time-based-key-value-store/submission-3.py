from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.key_value = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_value:
            self.key_value[key].append((timestamp, value))
        else:
            self.key_value[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value:
            return ""
        values = self.key_value[key]
        idx = bisect_right(values, timestamp, key=lambda x: x[0])
        if idx > 0:
            return values[idx - 1][1]
        return ""
