# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        count = 0

        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        num = count - n

        if num == 0:
            head = head.next
            return head

        curr = head
        while num > 1:
            curr = curr.next
            num -= 1
        
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return head

