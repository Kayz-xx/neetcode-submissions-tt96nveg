class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        col = {}
        for char in s:
            col[char] = col.get(char, 0) + 1;
        
        for char in t:
            if char in col:
                col[char] -= 1;
                if col.get(char) < 0:
                    return False
            else:
                return False

        return True
