# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        head_temp = head
        while head_temp:
            temp = head_temp.next
            head_temp.next = previous
            previous = head_temp
            head_temp = temp
        return previous