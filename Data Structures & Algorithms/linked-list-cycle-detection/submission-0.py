# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = set()
        while head:
            if head.val in count:
                return True
            count.add(head.val)
            head = head.next
        
        return False
            
        