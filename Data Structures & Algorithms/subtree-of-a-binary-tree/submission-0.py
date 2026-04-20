# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if self.areSame(node, subRoot):
                    return True
                return dfs(node.left) or dfs(node.right)
            return False

        return dfs(root)
        
    def areSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val == q.val:
                return self.areSame(p.left, q.left) and self.areSame(p.right, q.right)
            return False
        
        if not p and not q:
            return True

        return False