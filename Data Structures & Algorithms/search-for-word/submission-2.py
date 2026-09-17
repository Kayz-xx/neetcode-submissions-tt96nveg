class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        we have a board and a word, and we want to return a 
        boolean if that word exists within the board. 
        we can only move left, right, up and down.
        the challenge is which element we start at

        my approach would be to run binary search to first
        find the position of the starting character, once
        we have those positions. we can backtrack from
        each of those and see if a solution exists.
        if it does then we are sucessfull, else not

        define a hash set to avoid revisiting the same cell
        explore every path by going in all 4 directions
        '''
        visited = set()
        def backtrack(row, col, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]) or board[row][col] != word[i] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            found = (backtrack(row + 1, col, i + 1) 
            or backtrack(row - 1, col, i + 1) 
            or backtrack(row, col + 1, i + 1) 
            or backtrack(row, col - 1, i + 1))
            visited.remove((row, col))
            
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
                    
        return False