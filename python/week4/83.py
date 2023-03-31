# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head
        while r and r.next:
            if r.val == r.next.val:
                r.next = r.next.next
            else:
                r = r.next
        return head