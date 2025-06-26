# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        result = ListNode(0,head)
        current = result

        for _ in range(n):
            head = head.next

        while head:
            current = current.next
            head= head.next

        current.next = current.next.next

        return result.next