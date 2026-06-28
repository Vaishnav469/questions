# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 or list2:
            if not list2:
                curr.next = list1
                break
            elif not list1:
                curr.next = list2
                break
            elif list1.val < list2.val:
                curr.next = list1
                temp = list1.next
                list1.next = None
                list1 = temp
                curr = curr.next
            else:
                curr.next = list2
                temp = list2.next
                list2.next = None
                list2 = temp
                curr = curr.next
        return head.next

