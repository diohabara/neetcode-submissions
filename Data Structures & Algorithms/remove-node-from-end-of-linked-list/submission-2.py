class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
        head = reverse(head)
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        for _ in range(n - 1):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return reverse(dummy.next)