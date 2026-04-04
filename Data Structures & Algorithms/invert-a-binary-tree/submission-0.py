# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                popped = queue.popleft()
                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)
                popped.left, popped.right = popped.right, popped.left

        return root