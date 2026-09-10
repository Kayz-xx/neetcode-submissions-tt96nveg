# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == p or root == q: # if current node is p or q
            return root # then return the root
        
        left = self.lowestCommonAncestor(root.left, p, q) # check left tree
        right = self.lowestCommonAncestor(root.right, p, q) # check right tree
        # if p and q are in two different trees, then current node is the LCA
        # this is because we are recursing in order, so if this is true at 
        # anytime we immediately return the root
        if left and right:
            return root
        # if they are in one subtree
        # repeat the same process for that tree
        if left:
            return left
        if right:
            return right
        
        return None
        