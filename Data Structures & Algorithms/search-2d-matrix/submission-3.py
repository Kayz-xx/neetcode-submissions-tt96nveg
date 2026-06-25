class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        we are simply trying to run binary 
        search on nested arrays

        one approach would be to combine the arrays
        but that would involve a whole iteration to join different arrays
        instead we can use some kind of math to find the indices of different
        elements? convert (0, 0) -> (3,3) to [0, 11]?
        '''
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True

        return False