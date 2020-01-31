#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (63.30%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 60.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
# 
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
            
        # 层级index
        level = 0
        # 用二维数组构成的扁平树，元素是每一个层级index下的所有节点
        tree = [[root]]
        while level < len(tree):
            # 获取当前level所有的节点
            nodes = tree[level]
            # 收集下一层level的所有节点
            subnodes = []
            for node in nodes:
                if node.left:
                    subnodes.append(node.left)
                if node.right:
                    subnodes.append(node.right)
            if len(subnodes):
                tree.append(subnodes)
            # 更新level
            level += 1

        # 倒叙收集
        array = []
        for nodes in reversed(tree):
            subarr = []
            for node in nodes:
                subarr.append(node.val)
            array.append(subarr)

        return array
        
# @lc code=end

