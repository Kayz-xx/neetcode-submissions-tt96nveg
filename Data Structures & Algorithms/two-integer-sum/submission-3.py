class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i in range(len(nums)):
            indexes[nums[i]] = i
        
        for i, n in enumerate(nums):
            to_find = target - n
            if to_find in indexes and indexes[to_find] != i:
                return [i, indexes[to_find]]
        return []
