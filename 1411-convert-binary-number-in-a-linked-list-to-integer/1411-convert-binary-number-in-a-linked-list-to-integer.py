# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = head.val

        while head.next:
            num = num * 2 + head.next.val
            head = head.next

        return num        

        
        