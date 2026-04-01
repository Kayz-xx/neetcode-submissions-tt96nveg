class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        s_count = {}
        t_count = {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        res, res_len = [-1, -1], float('inf')
        have, need = 0, len(t_count)
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in t_count:
                s_count[char] = 1 + s_count.get(char, 0)
                if s_count[char] == t_count[char]:
                    have += 1
            
            while have == need:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                if s[left] in t_count:
                    s_count[s[left]] -= 1
                    if s_count[s[left]] < t_count[s[left]]:
                        have -= 1
                left += 1
            

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
