# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()

        curr, curr2 = list1, list2
        curr3 = head

        while curr and curr2:
            if curr.val <= curr2.val:
                curr3.next = ListNode(curr.val)
                curr = curr.next
            else:
                curr3.next = ListNode(curr2.val)
                curr2 = curr2.next

            curr3 = curr3.next

        if curr:
            curr3.next = curr
        if curr2:
            curr3.next = curr2

        return head.next