class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0 
        size = 0
        maxFreq = 0
        for right in range(len(s)):
            char = s[right]
            freq[char] += 1
            maxFreq = max(maxFreq, freq[char])

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            
            size = max(size, right - left + 1)
        
        return size

