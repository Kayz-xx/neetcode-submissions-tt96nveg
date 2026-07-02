class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        we want to search the minimum value in
        logarithmic time, in a rotated sorted array

        instead of O(n) approach we can use a binary
        search with modified conditions to move our 
        pointer. we can see that the distance between
        minimum and maximum value is always 1 index,
        even if that's wrapped around the array. [i+1] / length
        so we need to use that kind of logic here
        so do i use the values at the two pointers itself?
        and move mid in the direction of the lower values?
        '''

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]