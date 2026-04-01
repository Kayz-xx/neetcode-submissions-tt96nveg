class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can obviously use binary search here
        # i'm just thinking how we seperate the rows and columns
        # do i just combine them and run binary search?
        # but that's not optimal, for sure
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return True

        return False
        