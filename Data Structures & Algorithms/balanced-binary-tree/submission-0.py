class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left is False or right is False or abs(left - right) > 1:
                return False
            return 1 + max(left, right)
        return dfs(root) is not False