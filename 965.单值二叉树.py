#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归法
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        def isMatch(node, val):
            if node is None:
                return True
            if node.val != val:
                return False
            return isMatch(node.left, val) and isMatch(node.right, val)
        
        return isMatch(root, root.val)

# 迭代法
class Solution1:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        stack = [root]
        while len(stack):
            node = stack.pop()
            if node.val != val:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True

# @lc code=end

