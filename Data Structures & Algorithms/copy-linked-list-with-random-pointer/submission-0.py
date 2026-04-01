"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
        def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            if not head:
                return None
            m = {}
            curr = head
            while curr:
                m[curr] = Node(curr.val)
                curr = curr.next
            
            curr = head
            while curr:
                old = curr
                new = m[curr]

                new.next = m.get(old.next)
                new.random = m.get(old.random)

                curr = curr.next
            
            return m[head]
