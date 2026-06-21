class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        first, end = 0, len(s)-1
        while first <= end:
            if s[first].lower() != s[end].lower():
                return False
            first += 1
            end -= 1
        return True