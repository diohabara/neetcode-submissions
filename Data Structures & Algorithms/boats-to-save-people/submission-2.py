class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        l, r = 0, len(people)-1
        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1
            count += 1
            r -= 1
        return count