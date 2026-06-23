# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        we want to remove a node from end 
        of the linkes list, based on the 
        number n, so we start counting from the
        LAST node

        naive way would be, reverse, remove node, reverse again
        but that has two redundant operations
        so can do one forward pass, build a new linked list
        and skip the nth node from the end? 
        however to skip that particular node we would 
        need the length of the node first
        '''
        dummy = ListNode()
        dummy.next = head
        
        length = 0
        curr = dummy
        while curr:
            length += 1
            curr = curr.next

        index = 0
        curr2 = dummy
        while index + 1 < length - n:
            curr2 = curr2.next
            index += 1
        
        curr2.next = curr2.next.next if curr2.next else None

        return dummy.next





        