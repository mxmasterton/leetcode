# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return -1
            else:
                left_height = 1 + dfs(node.left)
                right_height = 1 + dfs(node.right)
                diameter = left_height + right_height
                result = max(diameter, result)
                return max(left_height, right_height)

        dfs(root)
        return result