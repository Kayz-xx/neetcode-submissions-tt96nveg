class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        we have an array of integers nums that contains
        n + 1 integers in the range [1, n]. there is 
        one repeated integer that we need to find. we 
        need to do this WITHOUT modifying the array and 
        using constant space (no data structure).

        one way to do this is with some kind of bit manipulation,
        since the bits of the repeated integer are identical. i 
        was thinking we can use the sum of the arrays because we know
        the total of [1, n]. the problem is that gives us if we have a 
        duplicate but not the duplicate itself. we will use the two pointer
        approach to detect a cycle by treating nums[i] as the next index, 
        turning this into a cyclic linked list detection problem
        '''
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


        return -1
        