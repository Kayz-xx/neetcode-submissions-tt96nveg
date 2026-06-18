class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        we're checking if a string is a palindrome
        this is pretty standard, have done this before

        we can replace whitespaces and lowercase the entire string
        then process using two pointers
        '''
        if not s:
            return False
        updated = []
        for char in s:
            if char.isalnum():
                updated += char.lower()
        s = "".join(updated)
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False

            left += 1
            right -= 1
            
        
        return True
