class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alnum
        arr = [c.lower() for c in s if c.isalnum() and c != " "]
        n = len(arr)
        for i in range(n):
            if arr[i] != arr[n-1-i]:
                return False
        return True