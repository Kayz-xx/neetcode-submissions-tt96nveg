# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        we're trying to find the diameter of the binary tree
        where diameter is nothing but the length of the longest
        path between any two nodes within a tree, it doesn't need
        to pass the root

        we need to use recursion, possibly use a helper function
        to find the actual depth of each node and then find the 
        global maximum after finding local max using max(left depth, right depth)
        but that would need me to process each node individually,
        '''
        self.max_diameter = 0
        def treeDiameter(root):
            if not root:
                return 0
            left = treeDiameter(root.left)
            right = treeDiameter(root.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        treeDiameter(root)
        return self.max_diameter