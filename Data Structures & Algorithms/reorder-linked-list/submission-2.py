# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        tmp = []
        cur = head
        while cur:
            tmp.append(cur)
            cur = cur.next
        i, j = 0, len(tmp)-1
        while i < j:
            tmp[i].next = tmp[j]
            i += 1
            if i == j:
                break
            tmp[j].next = tmp[i]
            j -= 1
        tmp[i].next = None