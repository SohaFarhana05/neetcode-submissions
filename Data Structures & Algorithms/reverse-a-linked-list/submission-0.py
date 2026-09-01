# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one , two , three = None, head, None
        while two:
            three = two.next
            two.next=one
            one = two
            two=three
        return one