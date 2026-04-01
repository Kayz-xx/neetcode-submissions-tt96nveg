class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated = ""
        for char in s:
            if char.isalnum():
                updated += char
        s = updated
        l, r = 0, len(s) - 1
        print(s)
        while l <= r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True