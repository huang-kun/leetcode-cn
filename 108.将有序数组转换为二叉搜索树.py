#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (67.94%)
# Likes:    309
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 65.1K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定有序数组: [-10,-3,0,5,9],
# 
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
    # 递归法：
    #
    # 根据二叉搜索树的特点：
    # 1. 节点的左子树只包含小于当前节点的数。
    # 2. 节点的右子树只包含大于当前节点的数。
    # 3. 所有左子树和右子树自身必须也是二叉搜索树。
    # 
    # 意思是，二叉搜索树中，左子树里任何一个节点的值都小于根节点的值，而
    # 右子树里任何一个节点的值，都大于根节点的值。
    # 
    # 对于一个有序数组来说，并且是由小到大的生序排列，关键就是找到中间值，
    # 因为中间值左边的任何一个值都小于中间值，右边任何一个值都大于中间值，
    # 于是中间值就成了二叉搜索树的根节点，其左子树的根节点就可以从中间值
    # 左边的数组中继续寻找，右子树的根节点就从中间值右边的数组里继续寻找。
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """传入一个列表，将列表的中间值作为树的根节点返回"""
        if len(nums) == 0:
            return None
        
        mid = len(nums) // 2
        val = nums[mid]
        
        node = TreeNode(val)
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node
        
# @lc code=end

