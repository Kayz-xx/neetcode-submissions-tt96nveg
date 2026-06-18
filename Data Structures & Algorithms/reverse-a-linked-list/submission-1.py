# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        ahh the class linked list reversal
        we need to reverse a linked list

        a linked list is made up of pointers
        there's no way we can look behind
        in singly linked list
        so we have to use a prev pointer to switch
        thus we need a temp variable to store the prev
        as once we still need a reference to the next node
        '''

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev