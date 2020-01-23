#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.97%)
# Likes:    379
# Dislikes: 0
# Total Accepted:    61.5K
# Total Submissions: 216.3K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
#    5
#   / \
#  1   4
#     / \
#    3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root, None, None)
    
    def _isValidBST(self, root: TreeNode, minVal: int, maxVal: int) -> bool:
        """满足二叉搜索树的条件：minVal < root.val < maxVal"""
        if root is None:
            return True
        
        if minVal is not None and root.val <= minVal:
            return False
        
        if maxVal is not None and root.val >= maxVal:
            return False
        
        return self._isValidBST(root.left, minVal, root.val) and \
                self._isValidBST(root.right, root.val, maxVal)
        
# @lc code=end

# 比如二叉搜索树：
#  10
#  / \
# 5  15
#    / \
#   12 20
#
# 二叉搜索树的每个节点的值都是限制在一个(min, max)区间内的，
# 而min和max的值都是继承自父节点的，所以验证二叉搜索树的方法
# 就是：
# 1. 判断当前节点是否满足min < root.val < max
# 2. 如果当前节点满足条件，再去递归判断左右子节点
#    是否都满足条件，并且更新min和max
#
#         null<[10]<null
#             /    \
#           /        \
#         /            \
#  null<[5]<10      10<[15]<null
#                      /   \
#                    /       \
#                  /           \
#             10<[12]<15   15<[20]<null
