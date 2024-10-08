# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lo, hi):
            if not node:
                return True
            
            if lo < node.val < hi:
                return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)

            return False

        return dfs(root, -inf, inf)