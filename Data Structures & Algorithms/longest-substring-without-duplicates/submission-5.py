class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        we are returning the length of the
        longest substring with no duplicates

        we can start both pointers at the start of the string
        process each character and add it to a set. calculate
        the length using the different of the pointers. if we
        reach a character that is already seen, we reset left
        to the current right pointer and start a new process
        '''

        length = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            char = s[right]
            while char in seen:
                seen.remove(s[left])
                left += 1
            
            length = max(length, right - left + 1)
            seen.add(char)
        
        return length