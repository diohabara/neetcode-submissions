# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        while q:
            n = len(q)
            level_list = []
            for _ in range(n):
                node = q.popleft()
                if node:
                    level_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_list:
                res.append(level_list)
        return res