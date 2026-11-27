# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap((val, idx))
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heappush(heap, (lists[i].val, i))
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _, idx = heappop(heap)
            node = lists[idx]
            cur.next = node
            cur = cur.next
            lists[idx] = node.next
            if lists[idx] is not None:
                heappush(heap, (lists[idx].val, idx))
        return dummy.next