#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (71.42%)
# Likes:    397
# Dislikes: 0
# Total Accepted:    100.8K
# Total Submissions: 141.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxDepth(self, root):
        # 如果是空树，节点个数为0
        if root is None:
            return 0

        # 如果是叶子节点（没有子节点的节点），返回当前节点个数
        if root.left is None and root.right is None:
            return 1

        # 递归查找：该节点左子树的最大深度
        ld = self.maxDepth(root.left)

        # 递归查找：该节点右子树的最大深度
        rd = self.maxDepth(root.right)

        # 比较左右子树的深度结果，找出最大值，还要算上自身节点个数
        return max(ld, rd) + 1
    
    def maxDepth2(self, root):
        """二叉树的最大深度，非递归实现，深度优先搜索"""

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        # 记录最大深度（节点数）
        md = 0
        # 用栈来保存当前节点和它相应level的深度（节点数）
        #（如果换成用队列的话，就变成了广度优先搜索）
        stack = [(root, 1)]

        while len(stack) > 0:
            n, d = stack.pop()
            md = max(md, d)
            if n.left is not None:
                stack.append((n.left, d+1))
            if n.right is not None:
                stack.append((n.right, d+1))
        
        return md

# @lc code=end

