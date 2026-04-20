# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p, q = q, p

        current = root
        while True:
            if p.val <= current.val <= q.val:
                return current
            elif p.val < current.val:
                current = current.left
            elif p.val > current.val:
                current = current.right