class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        ahhh i remember this problem very well,
        spent a few hours before i knew two pointers :skull:
        okay so we're trying to find the maximum amount
        of water that can be stored between two blocks
        the constraint is that the height of water
        cannot be taller than the SHORTEST bar 

        again we initialize two pointers here
        along with a maximum variable
        we iterate through the list, finding the area "volume"
        of water by indices difference along with minimun constraint
        '''

        left, right = 0, len(heights) - 1
        maximum = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maximum = max(area, maximum)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return maximum