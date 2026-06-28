# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        if length == 1:
            return head.next
        
        nth = length - n
        if nth == 0:
            head = head.next
            return head
            
        i = 0
        prev = head
        curr = head.next
        while i < nth - 1:
            prev = curr
            curr = curr.next
            i+= 1
        prev.next = curr.next

        return head
        
