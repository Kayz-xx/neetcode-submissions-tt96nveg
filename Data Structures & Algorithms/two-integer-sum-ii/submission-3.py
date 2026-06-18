class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        we are trying to return the indices of two numbers
        that add up to a given target number, i1 cannot equal i2.
        we need unique elements

        we are given an array which is sorted
        so we can start both at first and last element of the array
        total the current sum, and move in the direction
        we need to get the target
        then return final indices
        '''

        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]