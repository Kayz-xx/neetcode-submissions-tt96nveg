class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        we are trying to check if the permuation of s1 
        lies within s2, so the substring can be rearranged
        
        we keep a window of size s1 while moving through s2
        then we need to evaluate elements within the window
        one way to do this is using a frequency map, but this
        would make the solution O((n - m) * m) where n is the length 
        of s2 and m is the legnth of s1. basically we are always
        stepping by the legnth of s2, 
        '''
        from collections import Counter
        s1_count = Counter(s1)
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            s2_count = Counter(s2[left:right + 1])
            if s1_count == s2_count:
                return True
            left += 1
            right += 1
        
        return False