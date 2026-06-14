class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return is_pal(l+1, r) or is_pal(l, r-1)
        return True