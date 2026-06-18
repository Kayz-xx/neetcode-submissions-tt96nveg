# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        we're checking if a linked list has a cycle

        i actually remember this one because it was unique
        we have to use a fast and slow pointer that move at 
        different speeds, and if they ever meet
        we have a cycle, because two pointers at different speeds 
        should never meet
        '''

        slow, fast = head, head
        index = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False