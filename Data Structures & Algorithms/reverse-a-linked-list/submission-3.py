# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        sentinel = head
        """
        P->None
        S->a->b->c

        P->a->None
        S->b->c

        ...
        P->c->...->None
        S->None
        """
        while sentinel:
            prev, sentinel.next, sentinel = sentinel, prev, sentinel.next
        return prev