class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        ahh the classic binary search once again
        O(log n) time as it splits the array into 
        half because the array is already sorted,
        faster than linear search because it can
        split work by half each time

        we use a middle pointer based on left, right
        where the boundaries changes based on the condition
        '''

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
