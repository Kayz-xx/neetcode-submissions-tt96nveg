# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        count = 1
        curr = head
        while curr.next:
            count += 1
            curr = curr.next

        index = count - n
        curr = dummy
        for i in range(index):
            curr = curr.next

        curr.next = curr.next.next
        
        return dummy.next
