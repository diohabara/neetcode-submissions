# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        cur = head
        while cur:
            nxt = cur.next # 次に進むために退避
            cur.next = prev # 矢印を反対にする
            prev = cur # prevを進める
            cur = nxt # curを進める
        return prev