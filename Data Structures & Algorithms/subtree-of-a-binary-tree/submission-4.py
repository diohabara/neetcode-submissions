# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(a, b):
            if a is None or b is None:
                return a is b
            return (
                a.val == b.val
                and issame(a.left, b.left)
                and issame(a.right, b.right)
            )

        if subRoot is None:
            return True
        if root is None:
            return False
        return (
            issame(root, subRoot)
            or self.isSubtree(root.right, subRoot)
            or self.isSubtree(root.left, subRoot)
        )