# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            length = len(queue)
            for i in range(length):
                popped = queue.popleft()

                if i == length - 1:
                    res.append(popped.val)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
    
        return res