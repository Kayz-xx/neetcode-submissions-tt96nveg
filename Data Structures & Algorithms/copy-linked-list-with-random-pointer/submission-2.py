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
        node_map = defaultdict()
        curr = head
        new_head = None

        while curr:
            new_node = Node(curr.val)
            if not new_head:
                new_head = new_node
            node_map[curr] = new_node
            curr = curr.next

        for old_node, new_node in node_map.items():
            new_node.next = node_map.get(old_node.next, None)
            new_node.random = node_map.get(old_node.random, None)


        return new_head