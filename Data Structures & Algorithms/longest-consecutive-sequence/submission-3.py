class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_count = 0

        for num in nums:
            count = 0
            if (num - 1) not in nums:
                count = 1
                while (num + count) in nums:
                    count += 1
            max_count = max(count, max_count)
        return max_count 
