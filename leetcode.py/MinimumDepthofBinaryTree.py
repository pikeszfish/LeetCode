# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        if (not root.left) and (not root.right):
            return 1
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0:
            return right_depth + 1
        elif right_depth == 0:
            return left_depth + 1
        else:
            return min(left_depth, right_depth) + 1