# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we have to traverse the tree breadth first
        # hence we'll be using a queue (deque)
        if not root:
            return []
        levels = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                popped = queue.popleft()
                level.append(popped.val)
                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)
            levels.append(level)
        
        return levels