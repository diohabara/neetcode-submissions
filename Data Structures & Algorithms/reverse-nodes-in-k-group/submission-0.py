# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next
        dummy = ListNode(0, head)
        group_prev = dummy
        while k <= n:
            prev = None
            cur = group_prev.next
            for _ in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tail = group_prev.next
            tail.next = cur
            group_prev.next = prev
            group_prev = tail
            n -= k
        return dummy.next