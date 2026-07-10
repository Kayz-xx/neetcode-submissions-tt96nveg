class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        okay now we're searching for a particular 
        element within a rotated sorted array

        we need to use binary search with modified conditions
        first we need to figure out which part of the array
        we're in, before the pivot or after. we use the same
        approach of finding a mid, then check which part of the
        array we're in, the smaller or larger part. accordingly
        we can move the mid close to the target?
        '''
        def find_pivot(nums):
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            
            return left

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid

            return -1

        pivot = find_pivot(nums)
        if target >= nums[pivot] and target <= nums[-1]:
            return binary_search(pivot, len(nums) - 1)
        else:
            return binary_search(0, pivot)

        
        
