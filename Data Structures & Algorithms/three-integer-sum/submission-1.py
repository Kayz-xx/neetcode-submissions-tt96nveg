class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        we are trying to return 3 numbers at different indices
        that add up to 0. similar to two sum but adds a constraint
        
        i don't think we need a hashmap to store indices
        we can loop through the list
        and then use two pointers to find solution
        '''
        nums.sort()
        res = []
        seen = set()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total < -nums[i]:
                    left += 1
                elif total > -nums[i]:
                    right -= 1
                else:
                    indices = (nums[i], nums[left], nums[right])
                    if indices not in seen:
                        res.append(indices)
                        seen.add(indices)
                    left += 1
                    right -= 1

        return res
                