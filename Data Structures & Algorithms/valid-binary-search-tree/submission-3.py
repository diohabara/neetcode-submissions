# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, mi, ma):
            if not root:
                return True
            val = root.val
            if val <= mi or ma <= val:
                return False
            return rec(root.left, mi, val) and rec(root.right, val, ma)
        return rec(root.left, float('-inf'), root.val) and rec(root.right, root.val, float('inf'))
        