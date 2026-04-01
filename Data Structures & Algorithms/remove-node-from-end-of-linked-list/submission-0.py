# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        count = 1
        curr = head
        while curr.next:
            count += 1
            curr = curr.next
        index = count - n
        curr = head
        prev = None
        if index > 0:
            for i in range(index):
                prev = curr
                curr = curr.next
            if curr:
                prev.next = curr.next
            else:
                prev.next = None
        else:
            head = head.next

        return head
