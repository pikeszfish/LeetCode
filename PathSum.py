# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return self.dfs(root, sum, 0)

    def dfs(self, root, sum, cursum):
        if not root:
            return False
        if (not root.left) and (not root.right):
            return cursum + root.val == sum

        return self.dfs(root.left, sum, cursum + root.val) or self.dfs(root.right, sum, cursum + root.val)

