class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = [(position[i], speed[i]) for i in range(len(position))]
        stack.sort()
        last_time = 0
        total_fleet = 0
        while stack:
            p, s = stack.pop()
            t = (target - p) / s # time to destination
            if last_time < t: # slower than last time, no merge
                last_time = t
                total_fleet += 1
        return total_fleet
