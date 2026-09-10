# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder=[1,2,3,4]
        inorder=[2,1,3,4]
        '''
        indices = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            index = indices[root_val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root

        return helper(0, len(inorder) - 1)