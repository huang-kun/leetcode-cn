#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        invLeft = self.invertTree(root.left)
        invRight = self.invertTree(root.right)
        
        root.left = invRight
        root.right = invLeft

        return root
        
# @lc code=end

