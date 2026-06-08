class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we are trying to find the longest non-duplicate
        # substring within a larger string
        # to handle duplicates we can use a seen set
        # if not s:
        #     return 0
        # seen = set()
        # left, right = 0, 0
        # size = 1

        # while left < len(s) and right < len(s):
        #     if s[right] in seen:
        #         left = right
        #         seen = set()
        #     size = max(size, right - left + 1)
        #     seen.add(s[right])
        #     right += 1
        # # the problem with this is that we're essentially
        # # wiping the slate clean when finding a duplicate
        # return size

        size = 0
        seen = set()
        for left in range(len(s)):
            for right in range(left, len(s)):
                if s[right] in seen:
                    seen = set()
                    break
                size = max(size, right - left + 1)
                seen.add(s[right])
                right += 1

        return size