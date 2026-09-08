# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodCount(root, max_so_far=float('-inf')):
            if not root:
                return 0
            
            is_good = 1 if root.val >= max_so_far else 0
            new_max = max(root.val, max_so_far)
            
            return is_good + goodCount(root.left, new_max) + goodCount(root.right, new_max)
        
        return goodCount(root)