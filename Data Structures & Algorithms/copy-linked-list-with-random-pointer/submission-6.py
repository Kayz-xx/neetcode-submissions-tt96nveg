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
        '''
        we are given the head of a linked list, but each node
        contains a random pointer which can point to any node.
        we need to a return a deep copy of the list. the challenge
        is creating the nodes and setting up the pointers between them

        first step would be actually creating the nodes
        3, 7, 4, 5
        3.next = 7
        3.random
        '''
        if not head:
            return None
        node_map = {}
        curr = head

        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        for old_node, new_node in node_map.items():
            new_node.next = node_map.get(old_node.next)
            new_node.random = node_map.get(old_node.random)


        return node_map[head]